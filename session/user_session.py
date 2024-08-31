# User session class
class UserSession:
    # Constructor
    def __init__(self, name):
        self.user_name = name
        self.user_categories_responses = {}