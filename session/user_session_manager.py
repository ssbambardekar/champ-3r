# Imports
from user_session import UserSession
from user_category_responses import UserCategoryResponses


# User session manager class
class UserSessionManager:
    # Statics
    user_sessions = {}      # Dictionary {user_name (string), UserSession (object)}

    # Constructor
    def __init__(self) -> None:
        pass

    # Start user session
    def start_user_session(self, user_name):
        user_session = UserSession(user_name)
        UserSessionManager.user_sessions[user_name] = user_session

    # Get user session
    def get_user_session(self, user_name):
        return UserSessionManager.user_sessions[user_name]
    
    # End user session
    def end_user_session(self, user_name):
        del UserSessionManager.user_sessions[user_name]

  # Update user question response
    def update_user_question_response(self, user_name, category_id, category_name, question_id, question_answer_id):        
        if category_id not in UserSessionManager.user_sessions[user_name].user_categories_responses:
            UserSessionManager.user_sessions[user_name].user_categories_responses[category_id] = UserCategoryResponses(category_id, category_name)

        user_session = UserSessionManager.user_sessions[user_name]
        user_category_responses = user_session.user_categories_responses[category_id]
        user_category_responses.user_question_responses[question_id] = question_answer_id