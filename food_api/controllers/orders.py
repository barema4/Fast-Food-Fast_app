from flask import jsonify, request
from flask.views import MethodView
from food_api.models.food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity,get_raw_jwt
import datetime

class NewOrder(MethodView):

    @jwt_required
    def post(self):

        if not request.json['order_name']:
            return jsonify({'message': " field should not be empty"}), 400

        if request.json["order_name"] == "":
            return jsonify({'message': 'place order'}), 400

        if request.json["price"] == "":
            return jsonify({'message': 'enter the price'}), 400
        
        user = get_jwt_identity()
        
        order = DatabaseConnection()
        new_order = order.insert_order(str(user[0]), request.json['order_name'],request.json['price'])

        if new_order == "order exits ":
            return jsonify({'message': "order not added"}), 401
        return jsonify({'message': new_order,'user':user}), 201



class GetHistory(MethodView):
    @jwt_required
    def get(self):
        user = get_jwt_identity()
        print(user)
        history = DatabaseConnection()
        order_list = history.order_history(user[0])
        if order_list == "No orders":
            return jsonify({"order": order_list}), 404

        return jsonify(order_list)
        



class GetOrders(MethodView):
    @jwt_required
    def get(self):
        user = get_jwt_identity()
        user_type=user[4]
        print(user_type)
        if user_type != "true":

            return jsonify(error='Unauthorized access for admin'), 401

        order_item = DatabaseConnection()
        order_list = order_item.all_orders()
        print(order_list)

        return jsonify({"order_list":order_list}),200
        

class GetSpecificOrders(MethodView):
    @jwt_required
    def get(self,order_id):
        user = get_jwt_identity()
        user_type = user[4]
        if user_type != "true":
            return jsonify(error='unauthorized access for admin'), 401


        order_item = DatabaseConnection()
        order_list =  order_item.get_one_order(order_id)
        if order_list == "No order available":
            return jsonify({"order": 'No specific order for this endpoint'}), 404
        return jsonify({"order_list":order_list})
        
class Update_order(MethodView):
    @jwt_required
    def post(self):
        user = get_jwt_identity()
        user_type = user[4]
        order_id = request.json["order_id"]
        order_status = request.json["order_status"]
        if user_type != "true":
            return jsonify({"item": 'Not authorized for this function'}), 401

        order = DatabaseConnection()
        message = order.update_status(order_id,order_status)


        return jsonify({"message": message}),200

