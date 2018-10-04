from flask import Flask
from api.routes.urls import GetRoutes
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.env = 'development'
app.testing = True
GetRoutes.fetch_routes(app)
app.config['JWT_SECRET_KEY'] = 'rubarema'
jwt = JWTManager(app)
if __name__ == '__main__':
    app.run(debug=True)
