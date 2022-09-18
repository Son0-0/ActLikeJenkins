from flask import Blueprint, request
from routes.update.controller import update

update_bp = Blueprint('update_bp', __name__)


@update_bp.route('/', methods=['POST'])
def act_like_jenkins() -> None:
    data = request.get_json()
    update.act(data)
