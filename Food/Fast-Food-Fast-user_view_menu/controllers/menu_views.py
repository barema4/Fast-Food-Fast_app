
from flask import jsonify, request
from flask.views import MethodView
from food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime

class GetMenu(MethodView):

    def get(self):
        menu = DatabaseConnection()
        menu_list = menu.all_menu()
        if menu_list == "No orders available":
            return jsonify({"menu": 'we do not have food on the menu'}), 404

        return jsonify({"menu_list": menu_list}),200

