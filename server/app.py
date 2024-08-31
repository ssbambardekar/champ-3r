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

from question_manager import QuestionManager
from user_session import UserSession


# App class
class App:
    # Constructor
    def __init__(self) -> None:
        self.question_manager = QuestionManager()
        self.user_session = None

    # Start user session
    def start_user_session(self, name):
        self.user_session = UserSession(name)
        
    # Get root categories
    def get_root_categories(self):
        return self.question_manager.get_root_categories()        

    # Get category with details
    def get_category_with_details(self, category_id):
        return self.question_manager.get_category_with_details(category_id)
  