import os
import json
import subprocess
from dotenv import load_dotenv
from utils.commit.commit import Commit
import utils.webhook.webhook as webhook

load_dotenv()

WEBHOOK_URL = os.environ.get('slack_webhook_url')
REPO_PATH = os.environ.get('repository_path')


def act(data: json):
    try:
        branch_info = data['ref'].split('/')[-1]
        repository_name = data['repository']['full_name']

        commit_message = data['commits'][0]['message']
        commiter = data['commits'][0]['committer']['name']

        child = subprocess.run(
            [f'bash {REPO_PATH}'], text=True, capture_output=True, shell=True)

        commit_info = Commit(repository_name=repository_name, branch_info=branch_info,
                             commiter=commiter, commit_message=commit_message)

        if len(child.stderr) != 0:
            webhook.error(WEBHOOK_URL, commit_info, child.stderr)
        else:
            webhook.send(WEBHOOK_URL, commit_info)
        return {'status_code': 200}
    except Exception as e:
        webhook.error(WEBHOOK_URL, commit_info, e)
