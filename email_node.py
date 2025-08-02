from typing import Dict
from tools.email_tool import fetch_icloud_emails, summarize_email, extract_numbers_from_text


def summarize_email_node(state: Dict) -> Dict:
    input_text = state["input"]
    num_emails = extract_numbers_from_text(input_text, default=3)

    try:
        emails = fetch_icloud_emails(num_emails)

        if not emails:
            state["output"] = "No emails found or failed to connect to iCloud."
            return state

        summaries = []
        for email_data in emails:
            summary = summarize_email(email_data)
            summaries.append(f"**{email_data['subject']}**\n{summary}")

        state["output"] = "\n\n".join(summaries)
    except Exception as e:
        state["output"] = f"Error fetching or summarizing emails: {e}"

    return state
