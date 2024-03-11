from flask import request, jsonify
from . import db
from .models import User
from flask import current_app as app

@app.route('/users', methods=['GET'])
def get_users():
    letter = request.args.get('letter', 'A')
    page = request.args.get('page', 1, type=int)
    per_page = 1000  # by default it's set to 20

    users_query = User.query.filter(User.firstname.startswith(letter)).order_by(User.firstname, User.lastname).paginate(page=page, per_page=per_page, error_out=False)
    users = users_query.items

    users_data = [{'firstname': user.firstname, 'lastname': user.lastname} for user in users]
    return jsonify(users_data)
