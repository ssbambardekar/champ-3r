# Question Answer class
class QuestionAnswer:
    # Constructor
    def __init__(self, id, text, description, points, question_id):
        self.id = id
        self.text = text
        self.description = description        
        self.points = points
        self.question_id = question_id