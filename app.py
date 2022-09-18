from dotenv import load_dotenv
from flask import Flask
from routes.update.update import update_bp

load_dotenv()

PORT_NUM = 5000  # OR os.environ.get('port_num')

app = Flask(__name__)
app.register_blueprint(update_bp, url_prefix='/update')

if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT_NUM, debug=True)
