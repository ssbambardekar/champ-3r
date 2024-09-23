# Imports
import sys
import os
from sys import argv

# Set imports path for datastore
root_path = os.path.dirname(os.path.dirname(argv[0]))
datastore_module_path = root_path + '/datastore'
sys.path.insert(0, datastore_module_path)

from datastore_manager import DataStoreManager    
from category_with_details import CategoryWithDetails
from question_with_details import QuestionWithDetails
from datacache import DataCache


# Question manager class
class QuestionManager:
    # Statics
    _datacache = DataCache()

    # Constructor
    def __init__(self) -> None:
        self.datastore_manager = DataStoreManager()
        self.initialize_datacache()
        
    # Initialize data cache
    def initialize_datacache(self):
        # Load categories with details
        categories = self.get_categories()
        for category in categories:
            self.get_category_with_details(category.id)

        # Load total max points
        self.get_total_max_points()

    # Get categories
    def get_categories(self):
        if len(QuestionManager._datacache.categories) == 0:
            QuestionManager._datacache.categories = self.datastore_manager.get_categories()

        return QuestionManager._datacache.categories
    
    # Get category with details
    def get_category_with_details(self, category_id):
        if category_id not in QuestionManager._datacache.category_with_details_by_category_id:
            # Build category with details    
            category = self.datastore_manager.get_category(category_id)
            category_with_details = CategoryWithDetails(category)

            # Build questions with details
            max_category_points = 0
            questions_with_details = []
            questions = self.datastore_manager.get_questions(category_id)
            for question in questions:
                question_with_details = QuestionWithDetails(question)
                max_category_points += question_with_details.max_points 
                category_with_details.questions_with_details = questions_with_details

                # Build and cache question answers
                question_with_details.question_answers = self.datastore_manager.get_question_answers(question.id)
                for question_answer in question_with_details.question_answers:
                    QuestionManager._datacache.question_answer_by_question_answer_id[question_answer.id] = question_answer

                # Cache question
                QuestionManager._datacache.question_with_details_by_question_id[question_with_details.id] = question_with_details

                questions_with_details.append(question_with_details)
                
            # Save max points for the category in cache
            QuestionManager._datacache.max_category_points_by_category_id[category_id] = max_category_points

            # Save category with details in cache
            QuestionManager._datacache.category_with_details_by_category_id[category_id] = category_with_details

        return QuestionManager._datacache.category_with_details_by_category_id[category_id]

    # Get max points for a given category
    def get_max_points_for_category(self, category_id):
        return  QuestionManager._datacache.max_category_points_by_category_id[category_id]

    # Get total max points 
    def get_total_max_points(self):
        total_max_points = 0
        if QuestionManager._datacache.total_max_points == 0:
            for category_id in QuestionManager._datacache.max_category_points_by_category_id:
                total_max_points += self.get_max_points_for_category(category_id)
            
            # Cache total max points
            QuestionManager._datacache.total_max_points = total_max_points

        return QuestionManager._datacache.total_max_points
    
    # Get question answer
    def get_question_answer(self, question_answer_id):
        return QuestionManager._datacache.question_answer_by_question_answer_id[question_answer_id]


# Debug Code
if __name__ == "__main__":
    question_manager = QuestionManager()    

    categories = question_manager.get_categories()
    for category in categories:        
        category_with_details = question_manager.get_category_with_details(category.id)
        print ("Category: ", category_with_details.id, ", ", category_with_details.name, ", ", category_with_details.description, ", ", category_with_details.group)

        max_points_for_category = question_manager.get_max_points_for_category(category_with_details.id)
        print (" Max points for Category ", category_with_details.name, ": ", max_points_for_category)

        for question_with_details in category_with_details.questions_with_details:
            print("Question: ", question_with_details.id, ", ", question_with_details.text, ", ", question_with_details.description, ", ", question_with_details.max_points, ", ", question_with_details.category_id)

            for question_answer in question_with_details.question_answers:
                print("Answers: ", question_answer.id, ", ", question_answer.text, ", ", question_answer.description, ", ", question_answer.points, ", ", question_answer.question_id)
    
    total_max_points = question_manager.get_total_max_points()
    print ("total max points: ", total_max_points)
        