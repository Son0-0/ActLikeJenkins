import requests
from datetime import datetime

def send(webhook_url, err_pos, err_name, err_message):
  now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  payload = {
    "text": "[ERROR]: " + err_pos,
    "blocks": [
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "Error: *" + err_pos + "*"
        }
      },
      {
        "type": "divider"
      },
      {
        "type": "section",
        "fields": [
          {
            "type": "mrkdwn",
            "text": "*Type:* ERROR"
          },
          {
            "type": "mrkdwn",
            "text": "*Name:* " + err_name
          },
          {
            "type": "mrkdwn",
            "text": "*Message:*\n" + err_message.strip()
          },
          {
            "type": "mrkdwn",
            "text": "*When:*\n" + str(now)
          }
        ]
      },
      {
        "type": "divider"
      }
    ]
  }
  requests.post(webhook_url, json=payload)