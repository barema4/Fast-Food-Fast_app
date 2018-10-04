# Food_database





FAST_FOOD_FAST app is an web based application hosted on heroku that allows people to order food at any time and pay elctonically.It reduuces the time spend on ordering food.


FAST-FOOD-FAST app has got backend develop of api endpoints that consists of Nine features and database
  * Create user accounts that can signin/signout from the app. 
  *  Place an order for food.
  *  Get list of orders.
  *  Get a specific order.
  *  Update the status of an order. 
  *  Get the menu.
  * Add food option to the menu.
  * View the order history  for a particular user.

 
 Prerequisites for FAST-FOOD-FAST api endpoints

 * vscode
 * python
 * Virtual environment
 * flask frame work
 * pytest--cov
 * pylint
 * pytest
 * Postman
 * gunicorn
 * coveralls
 * coverage
 *Flask-JWT-Extended
 *psycopg2
 *Werkzeug

 
 
 Installation of prerequisites

 * download and install vscode
 * download and install python(3.6.5)
 * download and virtual environment
 * use pip to install flask in the terminal
 * use pip to install pytest in the terminal
 * use pip to install pytest--cov inthe terminal
 * use pip to install pylint in the terminal
 * use pip to install coverage in the terminal
 * use pip to install coveralls
 * use pip to install Flask-JWT-Extended
 * use pip to install psycopg2
 * use pip to install Werkzeug
 
 Api endpoints and their Routes
 
* VERB                            endpoint                                 use
* POST                              /api/v2/user/auth/signup            Register a user
* POST                             /api/v2/user/auth/login              Login in
* POST                            /api/v2/user /users/orders          Place the order
* GET                            /api/v2/user/orders                   Get the order history for a particular user.
* GET                           /api/v2/orders/                       Get all orders
* GET                          /api/v2/orders/<orderId>              Fetch a specific order
* PUT                         /api/v2/orders/<orderId>              Update the status  of an order
* GET                        /api/v2/menu                          Get available menu
* POST                      /api/v2/menu                          Add a meal option to the menu.


Deployment

The system is deployed on github which is integrated with TravisCl for continuous integration 
then integrated with coverall.io to show the percentage of code that is tested the integrated 
with code climate for maintainability and finally hosted on heroku in order for the user(Developer) to use.

Versioning

 * I use git hub for versioning.

 Authors

*RUBAREMA SAM* -(https://github.com/barema4)
FOr any contribbution to the project , you can vist my repository and view my pull requests and leave comments
 Acknowledgments

* Thanks to Andela