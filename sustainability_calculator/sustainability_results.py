# Sustainability results class
class SustainabilityResults:
    # Constructor
    def __init__(self, user_name):
        self.user_name = user_name
        self.score_by_category_names = {}      # Dictionary {category_name (string), percentage score for category (int)}
        self.total_score = 0
