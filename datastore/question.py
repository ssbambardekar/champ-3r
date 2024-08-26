# Question class
class Question:
    def __init__(self, id, name, description, category_id, points):
        self.id = id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.points = points