# Imports
import sys
import os
from sys import argv

# Set imports path for datastore

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
datastore_module_path = root_path + '/datastore'
sys.path.insert(0, datastore_module_path)

from datastore_manager import DataStoreManager    
from category_with_details import CategoryWithDetails
from question_with_details import QuestionWithDetails
from datacache import DataCache


# Question manager class
class QuestionManager:
    # Statics
    datacache = DataCache()

    # Constructor
    def __init__(self) -> None:
        self.datastore_manager = DataStoreManager()
        datacache = DataCache()

    # Get root categories
    def get_root_categories(self):
        if len(QuestionManager.datacache.root_categories) == 0:
            QuestionManager.datacache.root_categories = self.datastore_manager.get_root_categories()

        return QuestionManager.datacache.root_categories
    
    # Get questions with details
    def get_questions_with_details(self, category_id):
        if category_id not in QuestionManager.datacache.questions_with_details_by_category_id:
            questions_with_details = []
            questions = self.datastore_manager.get_questions(category_id)
            for question in questions:
                question_with_details = QuestionWithDetails(question)
                question_with_details.question_answers = self.datastore_manager.get_question_answers(question.id)
                questions_with_details.append(question_with_details)

            QuestionManager.datacache.questions_with_details_by_category_id[category_id] = questions_with_details

        return QuestionManager.datacache.questions_with_details_by_category_id[category_id]
    
    # Get child categories with details - Note that this goes only 1 level deep (i.e. no nested child categories are supported)
    def get_child_categories_with_details(self, parent_category_id):
        if parent_category_id not in QuestionManager.datacache.child_categories_with_details_by_parent_category_id:
            child_categories_with_details = []
            child_categories = self.datastore_manager.get_child_categories(parent_category_id)
            for child_category in child_categories:
                child_category_with_details = CategoryWithDetails(child_category)
                child_category_with_details.questions_with_details = self.get_questions_with_details(child_category_with_details.id)
                child_categories_with_details.append(child_category_with_details)
            
            QuestionManager.datacache.child_categories_with_details_by_parent_category_id[parent_category_id] = child_categories_with_details

        return QuestionManager.datacache.child_categories_with_details_by_parent_category_id[parent_category_id]

    # Get category with details
    def get_category_with_details(self, category_id):
        if category_id not in QuestionManager.datacache.category_with_details_by_category_id:
            category = self.datastore_manager.get_category(category_id)
            category_with_details = CategoryWithDetails(category)
            category_with_details.questions_with_details = self.get_questions_with_details(category.id)
            category_with_details.child_categories_with_details = self.get_child_categories_with_details(category.id)

            QuestionManager.datacache.category_with_details_by_category_id[category_id] = category_with_details

        return QuestionManager.datacache.category_with_details_by_category_id[category_id]


# Debug Code
if __name__ == "__main__":
    question_manager = QuestionManager()    

    categories = question_manager.get_root_categories()
    for category in categories:        
        category_with_details = question_manager.get_category_with_details(category)
        print (category.name)

