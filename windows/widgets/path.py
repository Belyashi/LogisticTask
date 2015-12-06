import os

_path_to_this = '/'.join(os.path.abspath(__file__).split('/')[:-1]) + '/'


# Authorization #

LOGIN_WIDGET = _path_to_this + 'login_widget.ui'
SIGN_UP_WIDGET = _path_to_this + 'sign_up_widget.ui'
DRIVERS_FORM = _path_to_this + 'drivers_form.ui'
COMPANY_FORM = _path_to_this + 'company_form.ui'

# Organization #

ADD_GOOD_FORM = _path_to_this + 'add_good_form.ui'
ADD_ORDER_FORM = _path_to_this + 'add_order_form.ui'
ORGANIZATION_CHOICE = _path_to_this + 'organization_choice.ui'
ORGANIZATION_GOODS = _path_to_this + 'organization_goods.ui'
ORGANIZATION_INTERFACE = _path_to_this + 'organization_interface.ui'
ORGANiZATION_ORDERS = _path_to_this + 'organization_orders.ui'

# Driver #

DRIVER_INTERFACE = _path_to_this + 'driver_interface.ui'
