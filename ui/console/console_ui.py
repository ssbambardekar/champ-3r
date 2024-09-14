# Imports
import sys
import os
from sys import argv

# Set imports path for calculator
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(argv[0])))
else:
    root_path = os.path.dirname(argv[0])
datastore_module_path = root_path + '/server'
sys.path.insert(0, datastore_module_path)

from app import App


# Console UI class
class ConsoleUI:
    # Constructor
    def __init__(self) -> None:
        self.app = App()
        self.exit_character = 'x'
        self.user_name = None

    # Start user session    
    def start_user_session(self):
        print("Welcome to Champ-3r! Lets get you scored away!")        
        selection_made = False
        while (not selection_made):    
            try:
                self.user_name = input("Please enter your name: ")
                if (self.user_name is None or self.user_name == ''):
                    raise Exception()
                
                selection_made = True
            except Exception:
                continue

        self.app.start_user_session(self.user_name)

    # End user session    
    def end_user_session(self):
        print("All done! Have a fantastic day!")
        self.app.end_user_session(self.user_name)    

    # Show categories
    def show_categories(self):
        print("Here are various categories:")

        index = 1
        categories = self.app.get_categories()        
        for root_category in categories:
            print(index, "-", root_category.name)
            index += 1

        return categories    

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
                selected_index_str = input("Enter your selection (x=exit): ")
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
        category_with_details = self.app.get_category_with_details(category.id)
        if len(category_with_details.questions_with_details) > 0:
            for question_with_details in category_with_details.questions_with_details:
                question_answer = self.process_question(question_with_details)                
                self.app.update_user_question_response(self.user_name, category.id, question_with_details.id, question_answer.id)
        else:
            print("No questions associated with category!")

    # Show sustainability results
    def show_sustainability_results(self):
        sustainability_results = self.app.get_user_sustainability_score(self.user_name)

        print("")
        print("All done! Here are the results:")
        print("-------------------------------")
        print("User name: ", sustainability_results.user_name)

        print("Sustainability Scores by Category:")
        for score_by_category_name in sustainability_results.score_by_category_names:
            print("Category: ", score_by_category_name, ", Score: ", sustainability_results.score_by_category_names[score_by_category_name])
        
        print("Total Sustainability Score: ", sustainability_results.total_score)
        
    # Interact with user
    def interact_with_user(self):
        # Start user session
        self.start_user_session()

        # Show categories
        categories = self.show_categories()
        
        # Process root categories
        for category in categories:            
            self.process_category(category)
            break;

        # Show sustainability results
        self.show_sustainability_results()

        # End user session
        self.end_user_session()


# Main execution code
if __name__ == "__main__":
    # Interact with the user
    console_ui = ConsoleUI()
    console_ui.interact_with_user()