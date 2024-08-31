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

from question import Question    


# Question-With-Details class
class QuestionWithDetails(Question):
    # Constructor
    def __init__(self, question):
        Question.__init__(self, question.id, question.text, question.description, question.max_points, question.category_id)
        self.question_answers = []