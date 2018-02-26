from flask_login import UserMixin, login_user
from werkzeug.security import check_password_hash
#from manager import login_manager



#@login_manager.user_loader
#def load_user(username):
#    u = app.config['USER_COLLECTION'].find_one({"_id": username})
#    if not u:
#        return None
#    return User(u['_id'])


class User(UserMixin):
    def __init__(self, username):
        self._name = username
        self._email = user_email[username]
        self._data = user_data[username]

    def get_id(self):
        return self._name

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)
