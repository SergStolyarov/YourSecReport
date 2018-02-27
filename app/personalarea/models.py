from flask_login import UserMixin, login_user
from werkzeug.security import check_password_hash
from app import login_manager
from app.database import db


@login_manager.user_loader
def load_user(username):
    u = db.get_client(username)
    if not u:
        return None
    return User(u['login'])


class User(UserMixin):
    def __init__(self, username):
        self._user = db.get_client(username)
        self._name = self._user['login']
        self._email = self._user['mail']
        self._hash_pwd = self._user['password']
        self._services = self._user['target']

    def get_id(self):
        return self._name

    def check_password(self, password):
        return check_password_hash(self._hash_pwd, password)
