"""
This script is responsible for extracting emails from a specific Slack Channel

Written by Payam Azadi December 2019

Usage: python3 extract_email.py --help
"""

import click
import os
import slack
import time


def extract_emails_from_slack(slack_api_token, channel_id, member_limit):
    """
    Extract emails from a given Slack channel.

    :param slack_api_token: Slack API token.
    :param channel_id: Slack channel ID.
    :param member_limit: member quantity limit to return.

    :return emails: list of returned emails.
    """

    client = slack.WebClient(token=slack_api_token)
    channel_info = client.conversations_members(channel=channel_id, limit=member_limit)
    emails = []

    for member in channel_info["members"]:
        email = ""

        member_info = client.users_profile_get(user=f"{member}")

        # try for secondary email first for CIT/SD/etc
        if "fields" in member_info["profile"] and member_info["profile"]["fields"] is not None:
            if "XfMZHQCFTL" in member_info["profile"]["fields"]:
                email = member_info["profile"]["fields"]["XfMZHQCFTL"]["value"]

        # if no luck, try for regular email field
        if not email:
            if "email" in member_info["profile"]:
                email = member_info["profile"]["email"]

        # if nothing, we're screwed :)
        if email:
            print(email)
            emails.append(email)
        else:
            print(f"User {member_info['profile']['real_name']} has no email set.")

        # deal with rate limiting
        time.sleep(1)
    return emails


# setup click command lib
@click.command()
@click.option(
    '--channel_id',
    help='the slack channel ID e.g. CESJXA4MT',
    required=True)
@click.option(
    '--member_limit',
    help='member limit to return from channel (default=200)',
    default=200)
def main(channel_id, member_limit):

    # get token from the environment variable
    token = os.environ['SLACK_API_TOKEN']

    emails = extract_emails_from_slack(slack_api_token=token,
                                       channel_id=channel_id,
                                       member_limit=member_limit)
    print("\n\n\n\n\n\n")
    print(",".join(emails))


if __name__ == "__main__":
    main()
