# Imports
#
from datastore.datastore_manager import DataStoreManager    


# Question manager class
#
class QuestionManager:
    def __init__(self) -> None:
        self.datastore_manager = DataStoreManager()


    # Initialize db connection
    #     
    def initialize(self):
        try:
            datastore = os.getcwd() + "/datastore/champ-3r.db"  
            db_connection = sqlite3.connect(datastore)
            if (db_connection is None):
                raise Exception("Error in connecting to the data store as connection is null")
        
            return db_connection
        except Exception as ex:
            raise Exception("Error in connecting to the data store.") from ex


# Debug Code
#
if __name__ == "__main__":
    print ("test")