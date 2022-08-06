import requests
from datetime import datetime

Image = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"


def send(webhook_url, repository_name, branch_info, commiter, commit_message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        "text": "[actLikeJenkins][Success ✅]: " + f"Repository: {repository_name}",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Repository: *" + repository_name + "*\nBranch: *" + branch_info + "*"
                }
            },
            {
                "type": "section",
                "block_id": "sections567",
                "text": {
                    "type": "mrkdwn",
                    "text": ">*Commiter:* " + commiter + "\n>*Commit Message:* " + commit_message + "\n>*When:* " + str(now)
                },
                "accessory": {
                    "type": "image",
                    "image_url": Image,
                    "alt_text": "FREITAG"
                }
            }
        ]
    }
    requests.post(webhook_url, json=payload)


def error(webhook_url, repository_name, branch_info, commiter, commit_message, error_message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        "text": "[actLikeJenkins][Fail ❌]: " + f"Repository: {repository_name}",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Repository:* " + repository_name + "\n*Branch:* " + branch_info
                }
            },
            {
                "type": "section",
                "block_id": "sections567",
                "text": {
                    "type": "mrkdwn",
                    "text": ">*Commiter:* " + commiter + "\n>*Commit Message:* " + commit_message + "\n>*When:* " + str(now) + "\n>*Error Message:* " + error_message
                },
                "accessory": {
                    "type": "image",
                    "image_url": Image,
                    "alt_text": "FREITAG"
                }
            }
        ]
    }
    requests.post(webhook_url, json=payload)
