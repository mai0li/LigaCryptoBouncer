import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.channel-memberships.creator']

def authenticate_youtube_api():
    creds = None
    token_path = os.path.join('secrets', 'token.json')
    client_secrets_path = os.path.join('secrets', 'client_secret.json')
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_path, SCOPES)
            creds = flow.run_local_server(port=9090)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)

def list_membership_levels(youtube):
    request = youtube.membershipsLevels().list(
        part='snippet'
    )
    response = request.execute()
    return response

def list_members(youtube):
    request = youtube.members().list(
        part='snippet',
        maxResults=100
    )
    response = request.execute()
    return response