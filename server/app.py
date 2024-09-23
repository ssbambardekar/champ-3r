# Imports
import sys
import os
from sys import argv

# Set imports path for calculator
root_path = os.path.dirname(os.path.dirname(argv[0]))
datastore_module_path = root_path + '/datamanager'
sys.path.insert(0, datastore_module_path)
datastore_module_path = root_path + '/session'
sys.path.insert(0, datastore_module_path)
datastore_module_path = root_path + '/sustainability_calculator'
sys.path.insert(0, datastore_module_path)

from question_manager import QuestionManager
from user_session_manager import UserSessionManager
from calculator import Calculator


# App class
class App:
    # Internal statics    
    _question_manager = QuestionManager()
    _session_manager = UserSessionManager()    
    _calculator = Calculator(_question_manager)

    # Constructor
    def __init__(self) -> None:
        pass

  # Get categories
    def get_categories(self):
        return App._question_manager.get_categories()        

    # Get category with details
    def get_category_with_details(self, category_id):
        return App._question_manager.get_category_with_details(category_id)
  
    # Start user session
    def start_user_session(self, user_name):
        App._session_manager.start_user_session(user_name)

    # End user session
    def end_user_session(self, user_name):
        App._session_manager.end_user_session(user_name)

    # Update user question response
    def update_user_question_response(self, user_name, category_id, question_id, question_answer_id):  
        category_with_details = self._question_manager.get_category_with_details(category_id)      
        App._session_manager.update_user_question_response(user_name, category_id, category_with_details.name, question_id, question_answer_id)

    # Get user sustainability score
    def get_user_sustainability_score(self, user_name):  
        return App._calculator.calculate_sustainability_score(App._session_manager.get_user_session(user_name))
  