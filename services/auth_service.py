class AuthService:
    def authenticate(self, user):
        # Mock authentication
        if user:
            return True
        raise Exception("Authentication failed")