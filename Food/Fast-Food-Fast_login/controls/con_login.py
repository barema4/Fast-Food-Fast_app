from flask import jsonify, request
from flask.views import MethodView
from food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime


class Login(MethodView):


    def post(self):

        keys = ("email", "password")

        if not set(keys).issubset(set(request.json)):
            return jsonify({'message': 'Empty feilds'}), 400

        if request.json["email"] == "":
            return jsonify({'message': 'Enter email'}), 400

        if (' ' in request.json['email']) == True:
            return jsonify({'message': 'Remove spaces in email'}), 400

        if request.json["password"] == "":
            return jsonify({'message': 'Enter password'}), 400

        user_login = DatabaseConnection()
        user = user_login.get_credentials(request.json['email'], request.json['password'])
        print(user)


        if user:

            return jsonify({
                "access_token": create_access_token(identity=user,expires_delta=datetime.timedelta(minutes= 25)),
                "message": "Login successful"
            }), 200

        return jsonify({"message": "Wrong email or password"}), 401
