import os

_path_to_this = '/'.join(os.path.abspath(__file__).split('/')[:-1]) + '/'


# Authorization #

LOGIN_WIDGET = _path_to_this + 'login_widget.ui'

SIGN_UP_WIDGET = _path_to_this + 'sign_up_widget.ui'
DRIVERS_FORM = _path_to_this + 'drivers_form.ui'
COMPANY_FORM = _path_to_this + 'drivers_form.ui'



