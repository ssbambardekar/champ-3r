# Imports
import json

# Category class
class Category:
    # Constructor
    def __init__(self, id, name, description, group):
        self.id = id
        self.name = name
        self.description = description
        self.group = group

    # Convert to json
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)    