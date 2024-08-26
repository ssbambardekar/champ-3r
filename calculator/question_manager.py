# Imports
import sys
import os
from sys import argv

# Set imports path for datastore
root_path = os.path.dirname(os.path.dirname(argv[0]))
datastore_module_path = root_path + '/datastore'
sys.path.insert(0, datastore_module_path)

from datastore_manager import DataStoreManager    


# Question manager class
class QuestionManager:
    def __init__(self) -> None:
        self.datastore_manager = DataStoreManager()


    # Get root categories
    def get_root_categories(self):
        return self.datastore_manager.get_root_categories()


    # Get child categories
    def get_child_categories(self, parent_category_id):
        return self.datastore_manager.get_child_categories(parent_category_id)


    # Get questions
    def get_questions(self, category_id):
        return self.datastore_manager.get_questions(category_id)


# Debug Code
if __name__ == "__main__":
    question_manager = QuestionManager()
    category_list = question_manager.get_root_categories()
    for category in category_list:        
        print (category.name)

        question_list = question_manager.get_questions(category.id)
        for question in question_list:
            print (question.name)                
        
        child_category_list = question_manager.get_child_categories(category.id)
        for child_category in child_category_list:        
            print (child_category.name)

            question_list = question_manager.get_questions(child_category.id)
            for question in question_list:
                print (question.name)                
