class User:
    def __init__(self):
        self.email = ""
        self.password = ""
        self.orders = []

    def set_password(self, password):
        if len(password) > 5:
            self.password = password
            return True
        else:
            return False

    def set_email(self, email):
        if "@gmail.com" in email or "@yahoo.com" in email:
            self.email = email
            return True
        else:
            return False

    def log_in(self, password):
        if password == self.password:
            return True
        else:
            return False
