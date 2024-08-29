# Imports
import sqlite3
import os


# Connect to the database
try:
    datastore = os.getcwd() + "/datastore/champ-3r.db"  
    db_connection = sqlite3.connect(datastore)
    if (db_connection is None):
        raise Exception("Error in connecting to the data store as connection is null")
except Exception as ex:
    raise Exception("Error in connecting to the data store.") from ex

# Initialize database
def create_categories():
    print(db_connection)

    # Create category table
    # #  
    cursor = db_connection.execute('''
        CREATE TABLE `category` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `name` TEXT UNIQUE, `description` TEXT, `parent_category_id` INTEGER REFERENCES `category`(`id`))
    ''')
    
    print(cursor.fetchall())

# Get datastore details
def get_datastore_details():
    print(db_connection)

    # Get all tables in the system
    #
    cursor = db_connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    print(cursor.fetchall())


# Debug Code
if __name__ == "__main__":
#    create_categories()
    get_datastore_details()
