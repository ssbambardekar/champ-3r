# Data cache class
class DataCache:
    # Constructor
    def __init__(self):
        self.categories = []        # List {Category (object)}
        self.category_with_details_by_category_id = {}      # Dictionary {category_id (int), CategoryWithDetails (object)}
        self.max_category_points_by_category_id = {}        # Dictionary {category_id (int), max category points (int)}
        self.question_with_details_by_question_id = {}      # Dictionary {question_id (int), QuestionWithDetails (object)}
        self.question_answer_by_question_answer_id = {}     # Dictionary {question_answer_id (int), QuestionAnswer (object)}        
        self.total_max_points = 0