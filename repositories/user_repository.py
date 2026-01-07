class UserRepository:
    def __init__(self):
        self._users = {}

    def add_user(self, user):
        self._users[user.user_id] = user

    def get_user(self, user_id):
        return self._users.get(user_id)