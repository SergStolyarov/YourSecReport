from flask_login import UserMixin, LoginManager
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    if username in user_credentials:
        return User(username)


class User(UserMixin):
    def __init__(self, username):
        self._name = username
        self._email = user_email[username]
        self._data = user_data[username]

    def get_id(self):
        return self._name
