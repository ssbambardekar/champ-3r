# Imports
import sys
sys.path.append('../datastore')
sys.path.append('../')

from datastore.question import Question


# Question-Answer class
class QuestionAnswer(Question):
    def __init__(self, id, name, description, category_id, points):
        Question.__init__(self, id, name, description, category_id, points)
        self.id = id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.points = points