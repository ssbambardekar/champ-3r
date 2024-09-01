# User category responses class
class UserCategoryResponses:
    # Constructor
    def __init__(self, category_id, category_name):
        self.category_name = category_name
        self.category_id = category_id
        self.user_question_responses = {}       # Dictionary {question_id (int), question_answer_id (int)}