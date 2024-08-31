# Imports
import sys
import os
from sys import argv

# Set imports path for datastore

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
datastore_module_path = root_path + '/datamanager'
sys.path.insert(0, datastore_module_path)

from question_with_details import QuestionWithDetails
from sustainability_results import SustainabilityResults


# Calculator class
class Calculator:
    # Constructor
    def __init__(self) -> None:
        pass

    # Calculate score
    def calculate_sustainability_score(self, user_session):
        sustainability_results = SustainabilityResults()
        
        return sustainability_results
