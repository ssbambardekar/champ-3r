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

from category import Category    


# Category-With-Details class
class CategoryWithDetails(Category):
    # Constructor
    def __init__(self, category):
        Category.__init__(self, category.id, category.name, category.description, category.parent_category_id)
        self.child_categories_with_details = []
        self.questions_with_details = []

