# Imports
import sys
import os
from sys import argv

# Set imports path for calculator
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
datastore_module_path = root_path + '/calculator'
sys.path.insert(0, datastore_module_path)

from question_manager import QuestionManager


# Console UI manager class
class ConsoleUIManager:
    def __init__(self) -> None:
        self.question_manager = QuestionManager()
        self.exit_character = 'x'

    # Show welcome message    
    def show_welcome_message(self):
        print("Welcome to Champ-3r! Lets get you scored away!")

    # Show and get root categories
    def show_and_get_root_categories(self):
        print("Here are root categories:")

        index = 1
        root_categories = self.question_manager.get_root_categories()        
        for root_category in root_categories:
            print(index, "-", root_category.name)
            index += 1

        return root_categories    

    # Proess question with details
    def process_question(self, question_with_details):
        # Show question details
        print("Question: ", question_with_details.text)
        print("Description: ", question_with_details.description)
        print("Answers Choices: ")
        selection_index = 1
        for question_answer in question_with_details.question_answers:
            print(selection_index, " - ", question_answer.text, " ", question_answer.description)
            selection_index += 1

        # Get user selection
        selection_made = False
        selected_index = 0
        while (not selection_made):    
            try:
                selected_index_str = input("Enter your selection (x=exit, b=back): ")
                if (selected_index_str == self.exit_character):
                    sys.exit(0)                
                selected_index = int(selected_index_str)
                if (selected_index == 0 or selected_index > len(question_with_details.question_answers)):
                    raise Exception()
                
                selection_made = True
            except Exception:
                continue
    
        return question_with_details.question_answers[selected_index - 1]
    
    # Proess category
    def process_category(self, category):
        # Process questions for the category
        print()
        print("Here are questions for category: ", category.name)
        category_with_details = self.question_manager.get_category_with_details(category)
        if len(category_with_details.questions_with_details) > 0:
            for question_with_details in category_with_details.questions_with_details:
                question_answer = self.process_question(question_with_details)
        else:
            print("No questions associated with category!")

        # Process child categories
        if len(category_with_details.child_categories_with_details) > 0:
            for child_category_with_details in category_with_details.child_categories_with_details:
                self.process_category(child_category_with_details)
    
    # Interact with user
    def interact_with_user(self):
        # Show root categories
        root_categories = self.show_and_get_root_categories()
        
        # Process root categories
        for root_category in root_categories:            
            self.process_category(root_category)
            break;
