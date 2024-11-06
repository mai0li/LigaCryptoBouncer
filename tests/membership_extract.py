import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from youtube.api import authenticate_youtube_api, list_members, list_membership_levels

youtube = authenticate_youtube_api()

# List membership levels
membership_levels = list_membership_levels(youtube)
print("Membership Levels:")
for level in membership_levels.get('items', []):
    print(f"Level ID: {level['id']}, Level Name: {level['snippet']['levelName']}")

# List members
members = list_members(youtube)
print("\nMembers:")
for member in members.get('items', []):
    print(f"Member ID: {member['snippet']['memberDetails']['channelId']}, Member Name: {member['snippet']['memberDetails']['displayName']}")