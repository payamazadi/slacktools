# Some Python scripts for doing handy Slack stuff.

To use, get a Slack token from from https://api.slack.com/docs/oauth-test-tokens  

And add it into your environment variables:  
```export SLACK_API_TOKEN=xoxp-...```

Install the Python requirements:  
```pip3 install -r requirements.txt```

* archivechannels.py - archives channels older than 120 (hardcoded) days
* archiveusers.py - delete users from Slack by Slack ID
* channel_list.py - get list of all public Slack channels
* slack_extract_email.py - pull emails from user profiles by Slack channel
* slackusers_private.py - mass invite all users from one slack channel into other slack channels

Maybe someday we can move these into a library and create a UI around it :)