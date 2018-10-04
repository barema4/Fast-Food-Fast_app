from flask import jsonify, request
from flask.views import MethodView
from api.models.food_model import DatabaseConnection
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime

class GetHistory(MethodView):
    @jwt_required
    def get(self):
        user = get_jwt_identity()
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
        if user_type != True:

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
        if user_type != True:
            return jsonify(error='unauthorized access for admin'), 401


        order_item = DatabaseConnection()
        order_list =  order_item.get_one_order(order_id)
        if order_list == "No order available":
            return jsonify({"order": 'No specific order for this endpoint'}), 404
        return jsonify({"order_list":order_list})

class Update_order(MethodView):
    @jwt_required
    def put(self,order_id):
        user = get_jwt_identity()
        user_type = user[4]
        if user_type != True:
            return jsonify({"item": 'Not authorized for this function'}), 401

        order = DatabaseConnection()
        order = order.update_status(order_id,request.json['order_status'])
        if order == "No order available":
            return jsonify({"order_status": 'order_status not updated'}),404
        return jsonify({"order_status":'status successfuly updated'}),200


        
