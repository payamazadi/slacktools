#######################
# Slack Tools
# Print list of all channels
# Written by Payam Azadi December 2019
#######################
import os
import slack
import requests
import time
from pprint import pprint

SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN'] # get one from https://api.slack.com/docs/oauth-test-tokens

client = slack.WebClient(token=SLACK_API_TOKEN)

channel_info = client.channels_list(exclude_archived="true")

for channel in channel_info["channels"]:
	print(channel["name"])