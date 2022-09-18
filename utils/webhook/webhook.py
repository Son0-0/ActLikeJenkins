import requests
from datetime import datetime
from utils.commit.commit import Commit

Image = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"


def send(webhook_url: str, commit_info: Commit) -> None:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        "text": "[actLikeJenkins][Success ✅]: " + f"Repository: {commit_info.repository_name}",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Repository: *" + commit_info.repository_name + "*\nBranch: *" + commit_info.branch_info + "*"
                }
            },
            {
                "type": "section",
                "block_id": "sections567",
                "text": {
                    "type": "mrkdwn",
                    "text": ">*Commiter:* " + commit_info.commiter + "\n>*Commit Message:* " + commit_info.commit_message + "\n>*When:* " + str(now)
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


def error(webhook_url: str, commit_info: Commit, error_message: str) -> None:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        "text": "[actLikeJenkins][Fail ❌]: " + f"Repository: {commit_info.repository_name}",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Repository:* " + commit_info.repository_name + "\n*Branch:* " + commit_info.branch_info
                }
            },
            {
                "type": "section",
                "block_id": "sections567",
                "text": {
                    "type": "mrkdwn",
                    "text": ">*Commiter:* " + commit_info.commiter + "\n>*Commit Message:* " + commit_info.commit_message + "\n>*When:* " + str(now) + "\n>*Error Message:* " + error_message
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
