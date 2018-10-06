import os
import time
import datetime
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

class DatabaseConnection():
    """
       Class for processing logic for endpoints for new user..
    """

    def __init__(self):
        
        params = (
            """
            CREATE TABLE IF NOT EXISTS "users" (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL UNIQUE,
                    password VARCHAR(200) NOT NULL,
                    User_type VARCHAR(10) DEFAULT 'FALSE'
                    

                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "orders" (                    
                    order_id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(user_id),
                    user_name VARCHAR(30) NOT NULL,
                    order_name VARCHAR(20) NOT NULL,
                    order_status VARCHAR(20) DEFAULT 'NEW' NOT NULL,
                    price VARCHAR(20) NOT NULL,
                    order_date date                                   

                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "items" (
                    item_id SERIAL PRIMARY KEY,
                    item VARCHAR(100) NOT NULL,
                    price VARCHAR(20) NOT NULL
                    
                    
                )
            """,)

        try:
            if (os.getenv("FLASK_ENV")) == "Production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
            else:
                self.connection = psycopg2.connect(dbname='andela',
                                                   user='postgres',
                                                   password='',
                                                   host='localhost',
                                                   port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            for param in params:
                self.cursor.execute(param)
        except(Exception, psycopg2.DatabaseError) as error:
            raise error

    def insert_new_user(self, user_name, email, password):

        self.cursor.execute("SELECT * FROM users WHERE email = %s", [email])
        check_email = self.cursor.fetchone()
        hashed_password = generate_password_hash(password, method='sha256')
        if check_email:
            return "email already exist"

        insert_item = "INSERT INTO users(user_name, email, password) VALUES('" + user_name + "', '" + email + "', '" + hashed_password + "')"
        self.cursor.execute(insert_item)
        return "Account created successfully"

    def get_credentials(self, email, password):

        self.cursor.execute("SELECT * FROM users WHERE email=%s",[email])
        user = self.cursor.fetchone()

        if user and check_password_hash(user[3], password):
                return user
        return None

    def insert_order(self,user_id, order_name,price):
        self.cursor.execute("SELECT user_name FROM users WHERE user_id= %s", [user_id])
        name = self.cursor.fetchone()
        print(name[0])

        time_value = time.time()
        date_time = datetime.datetime.fromtimestamp(time_value).strftime('%Y-%m-%d %H:%M:%S')


        insert_new_order = "INSERT INTO orders(user_id, user_name, order_name, price, order_date) VALUES('" + user_id+ "', '" +name[0]+ "','"+order_name+  "', '"+order_name+  "',  '" + date_time + "')"
        self.cursor.execute(insert_new_order)
        return "order succcssfully created"



    def order_history(self, user_id):
        
        self.cursor.execute("SELECT * FROM orders WHERE user_id = %s", [user_id])
        keys = ["order_id", "user_id", "user_name", "order_name", "order_status", "order_date"]

        orders = self.cursor.fetchall()
        

        order_list = []
        
        for order in orders:
            order_list.append(dict(zip(keys, order)))
            
        if not order_list:
            return "No order"
        return order_list

    def all_orders(self):

        order_in = "SELECT * FROM orders"
        self.cursor.execute(order_in)
        keys = ["order_id", "user_id","user_name", "order_name", "order_status", "order_date"]
        orders = self.cursor.fetchall()
       
        order_list = []
        for order in orders:
           
            order_list.append(dict(zip(keys, order)))

        return order_list

    def get_one_order(self, order_id):

        self.cursor.execute("SELECT * FROM orders WHERE order_id = %s", [order_id])
        keys = ["order_id", "user_id","user_name", "order_name", "order_status", "order_date"]
        order = self.cursor.fetchone()
        order_list = []
        if not order:
            return "Not available"

        else:
            order_list.append(dict(zip(keys, order)))
            return order_list


    def insert_item(self, item,price):

        insert_new_item = "INSERT INTO items(item,price) VALUES( '" + item+ "','" + price+ "')"
        self.cursor.execute(insert_new_item)
        return "item added succcssfully"

    def all_menu(self):

        menu_in = "SELECT * FROM items"
        self.cursor.execute(menu_in)
        keys = ["item_id","item","price"]
        menus = self.cursor.fetchall()
        menu_list = []
        for menu in menus:
            menu_list.append(dict(zip(keys, menu)))
            if not menu_list:
                return "No menu"
        return menu_list

    def update_status(self,order_id,order_status):
        self.cursor.execute(
            "UPDATE orders SET order_status = %s WHERE order_id = %s",[order_status,order_id]
        )

    def update_admin(self):
        self.cursor.execute("UPDATE users SET user_type ='true' WHERE user_id = 1")
    
