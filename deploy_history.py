#######################
# Slack Tools
# Get # of messages in #deployments
# Written by Payam Azadi August 2020
#######################
import os
import slack
import requests
from time import sleep
from pprint import pprint
from datetime import datetime

SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN'] # get one from https://api.slack.com/docs/oauth-test-tokens

client = slack.WebClient(token=SLACK_API_TOKEN)

CHANNEL = "C012ZNAB7K8"
MESSAGES_PER_PAGE = 100
MAX_MESSAGES = 1000000
page = 1
print("Retrieving page {}".format(page))
response = client.conversations_history(
    channel=CHANNEL,
    limit=MESSAGES_PER_PAGE,
)
assert response["ok"]
messages_all = response['messages']

# get the full channel history (paginated) and push onto messages_all
while len(messages_all) + MESSAGES_PER_PAGE <= MAX_MESSAGES and response['has_more']:
    page += 1
    print("Retrieving page {}".format(page))
    sleep(1)   # need to wait 1 sec before next call due to rate limits
    response = client.conversations_history(
        channel=CHANNEL,
        limit=MESSAGES_PER_PAGE,
        cursor=response['response_metadata']['next_cursor']
    )
    assert response["ok"]
    messages = response['messages']
    messages_all = messages_all + messages



freq = {}
# count up the frequency; # of messages per week #
for message in messages_all:
	if 'bot_id' in message.keys():
		messageTime = datetime.fromtimestamp(float(message["ts"]))
		messageTime1 = messageTime.strftime("%m/%d/%Y %V")
		messageWeek = messageTime.strftime("%V").__str__()
		
		if (messageWeek in freq): 
			freq[messageWeek] += 1
		else:
			freq[messageWeek] = 1

for key, value in freq.items(): 
    print ("% s : % d"%(key, value)) 