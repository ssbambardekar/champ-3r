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

        # get total max points
        total_max_points = self.question_manager.get_total_max_points()
        
        total_user_points = 0
        for category_id in user_session.user_categories_responses:
            # Get max points allowed for category
            max_points_for_category = self.question_manager.get_max_points_for_category(category_id)
            
            # Get sum of user points for each category
            user_points_for_category = 0
            user_category_responses = user_session.user_categories_responses[category_id]
            for question_id in user_category_responses.user_question_responses:
                question_answer = self.question_manager.get_question_answer(user_category_responses.user_question_responses[question_id])
                user_points_for_category += question_answer.points

            # Calculate user score for category 
            sustainability_results.score_by_category_names[user_category_responses.category_name] = user_points_for_category / max_points_for_category
            total_user_points += user_points_for_category

        # Calculate total user score
        sustainability_results.total_score = total_user_points / total_max_points

        return sustainability_results
