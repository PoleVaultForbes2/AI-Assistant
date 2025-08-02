# from langchain.tools import Tool
from datetime import datetime, timedelta
import os.path
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying scopes, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']


def authenticate_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


def add_event_to_calendar(title="New Event", start_time=None, duration_minutes=60):
    service = authenticate_calendar()

    if not start_time:
        # Default to one hour from now
        start_time = datetime.utcnow() + timedelta(hours=1)

    end_time = start_time + timedelta(minutes=duration_minutes)

    event = {
        'summary': title,
        'start': {
            'dateTime': start_time.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    return f"✅ Event created: {created_event.get('htmlLink')}"


# def add_to_calendar(_=None):
#     # In real usage, parse _ for datetime, title, etc.
#     return add_event_to_calendar(title="Meeting with Josh", duration_minutes=45)


# calendar_tool = Tool(
#     name="Calendar Tool",
#     func=add_to_calendar,
#     description="Use this to add an event to the user's calendar. Accepts a title, date, and time."
# )
