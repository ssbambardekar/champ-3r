# Imports
from sustainability_results import SustainabilityResults


# Calculator class
class Calculator:
    # Constructor
    def __init__(self, question_manager) -> None:
        self.question_manager = question_manager

    # Calculate score
    def calculate_sustainability_score(self, user_session):
        sustainability_results = SustainabilityResults(user_session.user_name)

        user_sustainability_score = 0
        total_max_points = self.question_manager.get_total_max_points()
        for user_category_responses in user_session.user_categories_responses:
            # Get max points allowed for category
            max_points_for_category = self.question_manager.get_max_points_for_category(user_category_responses.category_id)
            
        return sustainability_results
