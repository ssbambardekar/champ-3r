# Imports
import sys
import os
import json
from sys import argv

# Set imports path for datastore
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
datastore_module_path = root_path + '/datastore'
sys.path.insert(0, datastore_module_path)

from category import Category    


# Category-With-Details class
class CategoryWithDetails(Category):
    # Constructor
    def __init__(self, category):
        Category.__init__(self, category.id, category.name, category.description, category.group)        
        self.questions_with_details = []

    # Convert to json
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)    