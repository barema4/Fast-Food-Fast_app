from flask import Flask,jsonify
from food_api.urls.urls import GetRoutes
from flask_jwt_extended import JWTManager
from food_api.models.food_model import DatabaseConnection
app = Flask(__name__)
app.env = 'development'
GetRoutes.fetch_routes(app)
app.config['JWT_SECRET_KEY'] = 'rubarema'
jwt = JWTManager(app)

@app.errorhandler(404)
def Resource_out_found(error):
    return jsonify({'message':'Resource not found'}),404

@app.errorhandler(500)
def internal_server(error):
    return jsonify({'message':'sorry we couldnot process this process at this time'}),500

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'message':'That method is not allowed for this end point'}),405


@app.before_first_request
def create_admin():
    
    data =DatabaseConnection()
    data.update_admin() 

if __name__ == '__main__':
    app.run(debug=True)
