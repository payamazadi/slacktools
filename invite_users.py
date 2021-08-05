#######################
# Slack Tools
# Invite all users from comma separated OLD_CHANNEL_IDS to comma separated NEW_CHANNEL_IDS
# Preface a channel with p if it's a private channel, since these require different API methods
# Written by Payam Azadi December 2019
#######################
import os
import slack
import requests
import time
from pprint import pprint

SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN'] # get one from https://api.slack.com/docs/oauth-test-tokens
NEW_CHANNEL_IDS="C013JH95C77"
OLD_CHANNEL_IDS="CESJXA4MT"

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

def inviteUsers(channel):
	if channel.startswith("p"):
		channel_info = client.conversations_members(channel=channel[1:], limit=200)
	else:
		channel_info = client.channels_info(channel=channel,limit=200)["channel"]
	
	for member in channel_info["members"]:
		for newChannel in NEW_CHANNEL_IDS.split(","):
			if(newChannel.startswith("p")):
				response = requests.post('https://slack.com/api/conversations.invite?token=%s&users=%s&channel=%s' % (SLACK_API_TOKEN, member, newChannel[1:])).json()
			else:
				response = requests.post('https://slack.com/api/channels.invite?token=%s&user=%s&channel=%s' % (SLACK_API_TOKEN, member, newChannel)).json()
			
		pprint(response)
		time.sleep(1)

channels = OLD_CHANNEL_IDS.split(",")

for channel in channels:
	inviteUsers(channel)
