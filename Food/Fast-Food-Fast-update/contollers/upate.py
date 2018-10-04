from flask import jsonify, request
from flask.views import MethodView
from food_model import DatabaseConnection

from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

class Update_order(MethodView):
    @jwt_required
    def put(self, order_id):
        user = get_jwt_identity()
        user_type = user[4]
        if user_type != True:
            return jsonify({"item": 'Not authorized for this function'}), 401

        order = DatabaseConnection()
        order = order.update_status(order_id, request.json['order_status'])
        if order == "No order available":
            return jsonify({"order_status": 'order_status not updated'}), 404
        return jsonify({"order_status": 'status successfuly updated'}), 200

