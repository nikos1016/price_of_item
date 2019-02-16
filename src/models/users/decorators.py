from functools import wraps

from flask import session, url_for, redirect, request
from src.app import app

__author__ = 'nikosD'

def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        return func(*args, **kwargs) #func(...) args: func(5, 6) kwargs: func(x=5, y=6) args=unname kwargs=keyword argument
    return decorated_function

def requires_admin_permissions(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        if session['email'] not in app.config['ADMINS']:
            return redirect(url_for('users.login_user'))
        return func(*args, **kwargs) #func(...) args: func(5, 6) kwargs: func(x=5, y=6) args=unname kwargs=keyword argument
    return decorated_function

# @requires_login
# def my_funtion(x, y):
#     # print("Hello, world!")
#     return x + y
#
# print(my_funtion(5,6))