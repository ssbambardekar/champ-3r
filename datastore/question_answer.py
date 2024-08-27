# Question Answer class
class QuestionAnswer:
    def __init__(self, id, text, description, question_id, points):
        self.id = id
        self.text = text
        self.description = description        
        self.points = points
        self.question_id = question_id