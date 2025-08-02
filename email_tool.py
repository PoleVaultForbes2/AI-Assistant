# tools/email_tool.py
from langchain.tools import Tool
from email.header import decode_header
import imaplib
import email
import ollama
import socket
import re

# Set your credentials
EMAIL = "example@gmail.com"
PASSWORD = "bajk-fklj-example"


def extract_numbers_from_text(text: str, default: int = 3) -> int:
    match = re.findall(r"\b\d+\b", text)
    if match:
        return int(match[0])

    # fallback for word-based numbers
    word_map = {
        "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8,
        "nine": 9, "ten": 10, "a couple": 2, "a few": 3, "some": 4
    }

    text_lower = text.lower()
    for word, value in word_map.items():
        if word in text_lower:
            return value

    return default


def clean(text):
    return "".join(c if c.isalnum() else "_" for c in text)


def fetch_icloud_emails(limit):
    socket.setdefaulttimeout(10)
    imap = imaplib.IMAP4_SSL("imap.mail.me.com")

    try:
        imap.login(EMAIL, PASSWORD)
        imap.select("INBOX")
    except imaplib.IMAP4.error as e:
        print(f"Login failed: {e}")
        return []

    # Search for all emails
    status, messages = imap.search(None, "ALL")
    if status != "OK":
        print("Failed to search inbox.")
        return []

    email_ids = messages[0].split()[-limit:]
    emails = []

    for eid in email_ids:
        res, msg_data = imap.fetch(eid, "(BODY.PEEK[])")

        for response in msg_data:
            if not isinstance(response, tuple):
                continue

            msg = email.message_from_bytes(response[1])

            # Decode subject
            subject_raw = decode_header(msg["Subject"])[0]
            subject = subject_raw[0]
            if isinstance(subject, bytes):
                try:
                    subject = subject.decode(subject_raw[1] or "utf-8")
                except Exception:
                    subject = subject.decode(errors="ignore")

            from_ = msg.get("From", "(unknown)")

            # Extract the best available body
            body = None
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition") or "")

                    if "attachment" in content_disposition.lower():
                        continue

                    try:
                        payload = part.get_payload(decode=True)
                        if not payload:
                            continue
                        text = payload.decode(errors="ignore")

                        if content_type == "text/plain":
                            body = text
                            break  # Prefer plain text
                        elif content_type == "text/html" and not body:
                            body = text  # Fallback to HTML
                    except Exception as e:
                        print(f"⚠️ Error decoding part ({content_type}): {e}")
            else:
                try:
                    payload = msg.get_payload(decode=True)
                    body = payload.decode(errors="ignore")
                except Exception as e:
                    print(f"⚠️ Error decoding singlepart email: {e}")

            if body and body.strip():
                emails.append({
                    "from": from_,
                    "subject": subject,
                    "body": body.strip()[:1000]  # truncate to 1000 chars
                })
            else:
                print(f"❌ Skipped: No usable body from {from_} — Subject: {subject}")

    imap.logout()
    return emails


def summarize_email(email_data):
    prompt = f"""Summarize this email in 2–3 bullet points:
From: {email_data['from']}
Subject: {email_data['subject']}
Body:
{email_data['body']}
"""
    response = ollama.chat(
        model='mistral',  # or 'ollama3', 'gemma', etc.
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    return response['message']['content'].strip()
