from api.contollers.Authen import SignUp,Login,NewOrder
from api.contollers.menu import AddItem,GetMenu
from api.contollers.orders import GetHistory,GetOrders,GetSpecificOrders,Update_order

class GetRoutes():

    @staticmethod
    def fetch_routes(app):

        app.add_url_rule('/api/v2/auth/signup',
                         view_func=SignUp.as_view('Signup'), methods=['POST',])
        app.add_url_rule('/api/v2/auth/login',
                         view_func=Login.as_view('Login'), methods=['POST', ])
        app.add_url_rule('/api/v2/orders',
                         view_func=NewOrder.as_view('NewOrder'), methods=['POST', ])
        app.add_url_rule('/api/v2/users/orders',
                         view_func=GetHistory.as_view('GetHistory'), methods=['GET', ])
        app.add_url_rule('/api/v2/orders',
                         view_func=GetOrders.as_view('GetOrders'), methods=['GET', ])
        app.add_url_rule('/api/v2/orders',
                         view_func=GetSpecificOrders.as_view('GetSpecificOrders'), methods=['GET', ])

        app.add_url_rule('/api/v2/menu',
                         view_func=AddItem.as_view('AddItem'), methods=['POST', ])
        app.add_url_rule('/api/v2/menu',
                         view_func=GetMenu.as_view('GetMenu'), methods=['GET', ])
        app.add_url_rule('/api/v2/order/<int:order_id>',
                         view_func=Update_order.as_view('Update_order'), methods=['PUT', ])
