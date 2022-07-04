import os
import requests
import json
from flask import Flask, request

PORT_NUM = 5000
WEBHOOK_URL = ''  # Slack Incomming Webhook URL

app = Flask(__name__)


def send_webhook(msg):
    payload = {'text': msg}
    requests.post(WEBHOOK_URL, json=payload)


@app.route('/update', methods=['POST'])
def act_like_jenkins():
    data = request.get_json()
    try:
        os.system('./example.sh')
        send_webhook("Success")
    except:
        send_webhook("Fail")

    return {'status_code': 200}


if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT_NUM, debug=True)
