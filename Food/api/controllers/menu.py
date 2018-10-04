from flask import jsonify, request
from flask.views import MethodView
from api.models.food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime


class AddItem(MethodView):
    @jwt_required
    def post(self):

        if not request.json['item']:
            return jsonify({'message': " item_name field should not be empty"}), 400
        user = get_jwt_identity()
        user_type = user[4]
        if user_type != True:
            return jsonify({"item": 'Not authorized for this function'}), 404

        
        order = DatabaseConnection()
        new_item = order.insert_item(request.json['item'],request.json['price'])
        if new_item == "No item to add ":
            return jsonify({'message': "item not added"}), 401
        return jsonify({'message': new_item}), 201

class GetMenu(MethodView):

    def get(self):
        menu = DatabaseConnection()
        menu_list = menu.all_menu()
        if menu_list == "No orders available":
            return jsonify({"menu": 'we do not have food on the menu'}), 404

        return jsonify({"menu_list": menu_list}),200

