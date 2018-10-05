from flask import jsonify, request
from flask.views import MethodView
from food_api.models.food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime

class SignUp(MethodView):

    def post(self):

        keys = ("user_name", "email", "password")

        if not set(keys).issubset(set(request.json)):
            return jsonify({'message': 'You have  Empty feilds in your request'}), 400

        if request.json['user_name'] == "":
            return jsonify({'user_name': 'enter user_name'}), 400

        if (' ' in request.json['user_name']) == True:
            return jsonify({'message': 'Remove spaces in your user_name'}), 400

        if request.json['password'] == "":
            return jsonify({'message': 'Enter password'}), 400

        if (' ' in request.json['password']) == True:
            return jsonify({'Password': 'Remove spaces in password'}), 400

        if len(request.json['password']) < 6:
            return jsonify({'Password': 'Your password should be have 6 digits and above'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['email']):
            return jsonify({'email': 'Enter right format of email '}), 400

        data = DatabaseConnection()
        register_details = data.insert_new_user(request.json['user_name'], request.json['email'],
                                                request.json['password'])
        if register_details == "email already exits":
            return jsonify({'message': register_details}), 401

        return jsonify({'message': register_details}), 201


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

        