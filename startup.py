# Imports
import sys
import os
from sys import argv

# Set imports path for ui
root_path = os.path.dirname(argv[0])
datastore_module_path = root_path + '/ui'
sys.path.insert(0, datastore_module_path)

from console_ui_manager import ConsoleUIManager


# Interact with the user
console_ui_manager = ConsoleUIManager()
console_ui_manager.interact_with_user()