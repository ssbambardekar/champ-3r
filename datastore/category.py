# Category class
class Category:
    def __init__(self, id, name, description, parent_category_id):
        self.id = id
        self.name = name
        self.description = description
        self.parent_category_id = parent_category_id