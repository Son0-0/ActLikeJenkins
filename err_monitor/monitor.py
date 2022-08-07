import subprocess
import slack_webhook
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.environ.get('slack_webhook_url')

proc = subprocess.Popen(['tail', '-f', './out.log'], stdout=subprocess.PIPE)
for line in iter(proc.stdout.readline, '\n'):
  if not line: break
  else: 
    temp = str(line.rstrip(), 'utf-8')
    if '[ERROR]' in temp:
      try:
        err_log = temp.split('/')
        slack_webhook.send(WEBHOOK_URL, err_log[1], err_log[2], err_log[3])
      except:
        pass