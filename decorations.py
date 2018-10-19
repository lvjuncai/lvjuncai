from flask import session,redirect,url_for
from functools import wraps



def login_lim(func):
    @wraps(func)
    def wrapper(*args,**kargs):
        if session.get('user_id'):
            return func(*args,**kargs)
        else:
            return redirect(url_for('Login'))
    return wrapper
