# Question class
class Question:
    def __init__(self, id, text, description, max_points, category_id):
        self.id = id
        self.text = text
        self.description = description
        self.max_points = max_points        
        self.category_id = category_id