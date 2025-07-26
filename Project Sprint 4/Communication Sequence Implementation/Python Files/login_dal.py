# login_dal.py

class UserDataAccess:
    def __init__(self, filepath="users.txt"):
        self.filepath = filepath

    def load_users(self):
        users = {}
        try:
            with open(self.filepath, "r") as file:
                for line in file:
                    if ":" in line:
                        username, password = line.strip().split(":", 1)
                        users[username] = password
        except FileNotFoundError:
            print("User data file not found.")
        return users

    def add_user(self, username, password):
        with open(self.filepath, "a") as file:
            file.write(f"{username}:{password}\n")
