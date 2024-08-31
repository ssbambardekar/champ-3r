# Imports
import sys
import os
from sys import argv

# Set imports path for calculator
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
datastore_module_path = root_path + '/datamanager'
sys.path.insert(0, datastore_module_path)
datastore_module_path = root_path + '/session'
sys.path.insert(0, datastore_module_path)
datastore_module_path = root_path + '/sustainability_calculator'
sys.path.insert(0, datastore_module_path)

from question_manager import QuestionManager
from user_session import UserSession
from user_question_response import UserQuestionResponse
from calculator import Calculator


# App class
class App:
    # Statics
    question_manager = QuestionManager()
    user_sessions = {}
    calculator = Calculator()
        
    # Constructor
    def __init__(self) -> None:
        pass

  # Get root categories
    def get_root_categories(self):
        return App.question_manager.get_root_categories()        

    # Get category with details
    def get_category_with_details(self, category_id):
        return App.question_manager.get_category_with_details(category_id)
  
    # Start user session
    def start_user_session(self, user_name):
        user_session = UserSession(user_name)
        App.user_sessions[user_name] = user_session

    # End user session
    def end_user_session(self, user_name):
        del App.user_sessions[user_name]

    # Update user question response
    def update_user_question_response(self, user_name, category_id, question_id, question_answer_id):
        user_question_response = UserQuestionResponse(category_id, question_id, question_answer_id)
        App.user_sessions[user_name].user_question_responses.append(user_question_response)

    # get user sustainability score
    def get_user_sustainability_score(self, user_name):  
        return App.calculator.calculate_sustainability_score(App.user_sessions[user_name])
  