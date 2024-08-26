# Imports
import sqlite3
import os
from category import Category
from question import Question


# Datastore manager class
class DataStoreManager:
    def __init__(self) -> None:
        pass


    # Initialize db connection
    def initialize(self):
        try:
            datastore = os.getcwd() + "/datastore/champ-3r.db"  
            db_connection = sqlite3.connect(datastore)
            if (db_connection is None):
                raise Exception("Error in connecting to the data store as connection is null")
        
            return db_connection
        except Exception as ex:
            raise Exception("Error in connecting to the data store.") from ex


    # Get root categories
    def get_root_categories(self):
        try:            
            db_connection = self.initialize()

            # Get all the categories from data store
            cursor = db_connection.execute('''
                                           SELECT * FROM category 
                                           WHERE parent_category_id IS NULL;
                                           ''')
            rows = cursor.fetchall();
            db_connection.close();

            # Convert the rows into list of category objects
            category_list = []        
            for row in rows:
                category = Category(row[0], row[1], row[2], row[3])  
                category_list.append(category)

            return category_list
        except Exception as ex:
            raise Exception("Error in getting root categories from the data store.") from ex


    # Get child categories
    def get_child_categories(self, parent_category_id):
        try:            
            db_connection = self.initialize()

            # Get all the child categories related to a parent category from data store
            query_param = (int(parent_category_id),);
            cursor = db_connection.execute('''
                                           SELECT * FROM category 
                                           WHERE parent_category_id = ?;
                                           ''', query_param)
            rows = cursor.fetchall();
            db_connection.close();

            # Convert the rows into list of category objects
            category_list = []        
            for row in rows:
                category = Category(row[0], row[1], row[2], row[3])  
                print(category)

                category_list.append(category)

            return category_list
        except Exception as ex:
            raise Exception("Error in getting child categories from the data store.") from ex
        

    # Get questions
    def get_questions(self, category_id):
        try:            
            db_connection = self.initialize()

            # Get all the questions related to a category from data store
            query_param = (int(category_id),);
            cursor = db_connection.execute('''
                                           SELECT * FROM category_question 
                                           WHERE category_id = ?;
                                           ''', query_param)
            rows = cursor.fetchall();
            db_connection.close();

            # Convert the rows into list of question objects
            question_list = []        
            for row in rows:
                question = Question(row[0], row[1], row[2], row[3], row[3])  
                print(question)

                question_list.append(question)

            return question_list
        except Exception as ex:
            raise Exception("Error in getting questions from the data store.") from ex


# Debug Code
if __name__ == "__main__":
    datastoreManager = DataStoreManager()
    category_list = datastoreManager.get_root_categories()
    for category in category_list:        
        print (category.name)

        question_list = datastoreManager.get_questions(category.id)
        for question in question_list:
            print (question.name)                
        
        child_category_list = datastoreManager.get_child_categories(category.id)
        for child_category in child_category_list:        
            print (child_category.name)

            question_list = datastoreManager.get_questions(child_category.id)
            for question in question_list:
                print (question.name)                
