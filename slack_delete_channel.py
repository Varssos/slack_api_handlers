#!/usr/bin/python3

import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Twój token dostępu do Slacka
slack_token = "xoxb-...."

client = WebClient(token=os.environ.get(slack_token))
logger = logging.getLogger(__name__)
channel_id = "qwert"  # Identyfikator kanału lub czatu do usunięcia

try:
    # Wywołanie metody API conversations.archive w celu zarchiwizowania kanału
    result = client.conversations_archive(channel=channel_id)
    logger.info(result)

except SlackApiError as e:
    logger.error(f"Błąd podczas usuwania kanału: {e}")


# Investigate why:
# Błąd podczas usuwania kanału: The request to the Slack API failed. (url: https://www.slack.com/api/conversations.archive)
# The server responded with: {'ok': False, 'error': 'not_authed'}