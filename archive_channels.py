#######################
# Slack Tools
# Archive all public channels older than x number of days
# Written by Payam Azadi December 2019
#######################

import os
import slack
from pprint import pprint
from datetime import datetime
from time import sleep

def getLastRealMessage(channelHistory):
	for message in channelHistory["messages"]:
		if 'subtype' in message.keys():
			if message["subtype"] == "bot_message":
				return message
			continue
		return message

def archiveChannels(channels):
	count = 0
	archived = open("archived.log","a+")
	for channel in channels:
		channelId = channel["id"]
		channelName = channel["name"]
		channelHistory = client.channels_history(type="message",channel=channelId)
		
		lastMessage = getLastRealMessage(channelHistory)

		if lastMessage is None:
			archived.write("Manually archive " + channelName)
			continue
		if not "ts" in lastMessage.keys():
			archived.write("Manually archive " + channelName)
			continue
		
		lastMessageTime = datetime.fromtimestamp(float(lastMessage["ts"]))
		elapsed = (datetime.now() - lastMessageTime).days
		
		if elapsed > 21:
			try:
				client.channels_archive(channel=channelId)
				archived.write("Archived " + channelName + "(" + elapsed.__str__() + ")\n")
				print("Archived " + channelName + "(" + elapsed.__str__() + ")")
			except:
				archived.write("Failed to archive " + channelName + "\n")
				print("Failed to archive " + channelName)
			sleep(1)
			count+=1
		sleep(2)
	print("Archived " + count.__str__() + " channels.")
	archived.write("Archived " + count.__str__() + "channels.")
	archived.close()

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

response = client.channels_list(exclude_archived="true")
publicChannels = response["channels"]
archiveChannels(publicChannels)