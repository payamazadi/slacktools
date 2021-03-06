#######################
# Slack Tools
# Delete all users by Slack ID using the SCIM API
# Written by Payam Azadi December 2019
#######################
import os
import requests
from time import sleep

SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN']

users="U2HHCM95Z,U2K62C8Q3,U33SH8J65,U356905KL,U3MEKNZUM,U3MQ96GPN,U3N7TN35E,U3NC5KJNM,U3NTP589L,U3NUDCVM1,U3PK6JF7Y,U3QHZLLHE,U3RA21SF2,U3T0W17DZ,U3TP8NKN3,U3UF37LT0,U3UFXHFCY,U3V7BUX42,U3V9XPTQD,U3VT54FQE,U3WNG6TK2,U459FAD0D,U4BF5ECF2,U4E4XCLDU,U4EALS9AN,U4GPK3Q06,U4HUQQW1E,U4KEN4FM2,U4LTKS2E5,U4M8EAZQT,U4MAXTR98,U4TQJU7T7,U4U8CQWSJ,U4X213ELC,U4YDEU17Y,U5ACYRWSZ,U5JTCV8L9,U5KNLHP5G,U5R22QSAH,U67T10YEQ,U69DA4SSG,U6APT0QPQ,U6GVC5LP5,U6KS1TCQ1,U7GKHG142,U94L8H4G1,U95HUPWLX,U9JNL2KK3,U9L7AFZ5Y,U9P1MR1TN,U9ZQG8FQ9,UA0BBF0PL,UA7BUV319,UA7EGTLV6,UA7FTPSBE,UABE42X4G,UAFDJQP6G,UAJ8CGB4P,UATL9LSQG,UAUF8LDC5,UAUQZANRG,UAUV1NDV3,UAV5B20PQ,UAWSD68HF,UAZRWARU5,UB8MN4FK2,UC5UE9THQ,UDTM073D3,UF3ETAYF9,UL32SCWSU,UMK1G1E5D,UNU2JTCSV"
users_split = users.split(",")

headers = {'Authorization': 'Bearer ' + SLACK_API_TOKEN}
for user in users_split:
	print(user)
	deleteResponse = requests.delete(
		'https://api.slack.com/scim/v1/Users/%s' % (user),
	 	headers=headers
	 )
	print(deleteResponse)
	sleep(1)