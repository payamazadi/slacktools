#######################
# Slack Tools
# Download all Slack workspace emojis and put them into a folder
# Requires JSON file 
# Written by Payam Azadi December 2019
# Lifted mostly from hhttps://gist.github.com/lmarkus/8722f56baf8c47045621#gistcomment-2918675
# To import, use https://github.com/smashwilson/slack-emojinator. Set your .env file's SLACK_TEAM and SLACK_COOKIE and that should be enough.
#######################

import sys
from pprint import pprint
import json
import os
import urllib.request

if len(sys.argv) != 2:
    print('Usage: %s file.json' % sys.argv[0])
    sys.exit()

with open(sys.argv[1], 'r') as fp:
    obj = json.load(fp)
folder = 'emojis'

for emoji in obj["emoji"]:
    name = emoji
    url = obj['emoji'][name]
    try:
        if type(url) is dict:
            url = url["apple"]
        if url.find("alias") >= 0:
            print("Skipping " + name + " which has alias " + url)
        else:
            

            extensionIdx = url.rindex(".")
            extension = url[extensionIdx:]
            print(name + extension + "," + url)

            urllib.request.urlretrieve(url, folder + '/' + name + extension)
    except e:
        print("Failed " + name)
        print(e)