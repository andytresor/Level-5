from flask import Blueprint # type: ignore
from controllers.article_controller import index, view, delete, add_post, create, update


article = Blueprint('article', __name__)

article.route("/", methods=['GET'], strict_slashes=False)(index)
article.route("/add-post", methods=['GET'], strict_slashes=False)(add_post)
article.route('/create', methods=["POST"], strict_slashes=False)(create)
article.route('/view/<id>', methods=['GET'], strict_slashes=False)(view)
article.route('/delete/<id>', methods=["DELETE", "POST"], strict_slashes=False)(delete)
article.route('/update/<id>', methods=["POST", "GET"], strict_slashes=False)(update)