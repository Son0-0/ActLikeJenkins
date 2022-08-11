import subprocess
import requests
import json
import os
import slack_webhook
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

PORT_NUM = 5000  # OR os.environ.get('port_num')
# Slack Incomming Webhook URL
WEBHOOK_URL = os.environ.get('slack_webhook_url')
REPO_PATH = os.environ.get('repository_path')

app = Flask(__name__)


@app.route('/update', methods=['POST'])
def act_like_jenkins():
    data = request.get_json()
    
    try:
        branch_info = data['ref'].split('/')[-1]
        repository_name = data['repository']['full_name']

        commit_message = data['commits'][0]['message']
        commiter = data['commits'][0]['committer']['name']
      
        child = subprocess.run(
            [f'bash {REPO_PATH}'], text=True, capture_output=True, shell=True)
        if len(child.stderr) != 0 :
            slack_webhook.error(WEBHOOK_URL, repository_name,
                                branch_info, commiter, commit_message, child.stderr)
        else:
            slack_webhook.send(WEBHOOK_URL, repository_name,
                               branch_info, commiter, commit_message)
        return {'status_code': 200}
    except Exception as e:
        slack_webhook.error(WEBHOOK_URL, repository_name,
                            branch_info, commiter, commit_message, e)

if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT_NUM, debug=True)
