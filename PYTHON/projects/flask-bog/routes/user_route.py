from flask import Blueprint # type: ignore
from controllers.user_controller import index, view, add_user, newUser, update_user, delete_user

user = Blueprint('user', __name__)

user.route("/display", methods=['GET'], strict_slashes=False)(index)
user.route("/add_user", methods=['GET'], strict_slashes=False)(add_user)
user.route('/new', methods=["POST"], strict_slashes=False)(newUser)
user.route('/views/<id>', methods=['GET'], strict_slashes=False)(view)
user.route('/delet/<id>', methods=["DELETE", "POST"], strict_slashes=False)(delete_user)
user.route('/updat/<id>', methods=["POST", "GET"], strict_slashes=False)(update_user)