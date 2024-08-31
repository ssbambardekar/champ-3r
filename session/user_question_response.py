# User question response class
class UserQuestionResponse:
    # Constructor
    def __init__(self, category_id, question_with_detail_id, question_answer_id):
        self.category_id = category_id
        self.question_with_detail_id = question_with_detail_id
        self.question_answer_id = question_answer_id