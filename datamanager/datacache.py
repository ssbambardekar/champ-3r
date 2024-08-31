# Data cache class
class DataCache:
    # Constructor
    def __init__(self):
        self.categories = []
        self.category_with_details_by_category_id = {}
        self.max_category_points_by_category_id = {}
        self.question_with_details_by_question_id = {}
        self.question_answer_by_question_answer_id = {}        
        self.total_max_points = 0