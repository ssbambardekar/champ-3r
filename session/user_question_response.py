# User question response class
class UserQuestionResponse:
    # Constructor
    def __init__(self, name):
        self.user_name = name
        self.category = None
        self.question_with_detail = None
        self.question_answer = None