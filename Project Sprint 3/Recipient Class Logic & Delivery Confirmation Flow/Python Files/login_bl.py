# login_bl.py

from login_dal import UserDataAccess

class LoginManager:
    def __init__(self):
        self.data_access = UserDataAccess()

    def authenticate_user(self, username, password):
        users = self.data_access.load_users()
        return users.get(username) == password

    def register_user(self, username, password):
        users = self.data_access.load_users()
        if username in users:
            return False  # User already exists
        self.data_access.add_user(username, password)
        return True
