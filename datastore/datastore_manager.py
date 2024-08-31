# Imports
import sqlite3
import os
from category import Category
from question import Question
from question_answer import QuestionAnswer


# Datastore manager class
class DataStoreManager:
    # Constructor
    def __init__(self) -> None:
        pass

    # Initialize db connection
    def initialize(self):
        try:
            datastore = os.getcwd() + "/datastore/champ_3r.db"  
            db_connection = sqlite3.connect(datastore)
            if (db_connection is None):
                raise Exception("Error in connecting to the data store as connection is null")
        
            return db_connection
        except Exception as ex:
            raise Exception("Error in connecting to the data store.") from ex

    # Get categories
    def get_categories(self):
        try:            
            db_connection = self.initialize()

            # Get all the categories from data store
            cursor = db_connection.execute('''
                                           SELECT * FROM category;
                                           ''')
            rows = cursor.fetchall();
            db_connection.close();

            # Convert the rows into list of category objects
            categories = []        
            for row in rows:
                category = Category(row[0], row[1], row[2], row[3])  
                categories.append(category)

            return categories
        except Exception as ex:
            raise Exception("Error in getting categories from the data store.") from ex
        
    # Get category
    def get_category(self, category_id):
        try:            
            db_connection = self.initialize()

            # Get the requisite category from data store
            query_param = (int(category_id),);
            cursor = db_connection.execute('''
                                           SELECT * FROM category 
                                           WHERE id = ?;
                                           ''', query_param)
            rows = cursor.fetchall();
            db_connection.close();

            # Convert the rows into list of category objects            
            for row in rows:
                return Category(row[0], row[1], row[2], row[3])  

            return category
        except Exception as ex:
            raise Exception("Error in getting category from the data store. category_id: ", category_id) from ex        

    # Get questions
    def get_questions(self, category_id):
        try:            
            db_connection = self.initialize()

            # Get all the questions related to a category from data store
            query_param = (int(category_id),);
            cursor = db_connection.execute('''
                                           SELECT * FROM question 
                                           WHERE category_id = ?;
                                           ''', query_param)
            rows = cursor.fetchall();
            db_connection.close();

            # Convert the rows into list of question objects
            questions = []        
            for row in rows:
                question = Question(row[0], row[1], row[2], row[3], row[4])  
                questions.append(question)

            return questions
        except Exception as ex:
            raise Exception("Error in getting questions from the data store.") from ex
        
    # Get question answers
    def get_question_answers(self, question_id):
        try:            
            db_connection = self.initialize()

            # Get all the question answerss related to a question from data store
            query_param = (int(question_id),);
            cursor = db_connection.execute('''
                                           SELECT * FROM question_answer 
                                           WHERE question_id = ?;
                                           ''', query_param)
            rows = cursor.fetchall();
            db_connection.close();

            # Convert the rows into list of question answer objects
            question_answers = []        
            for row in rows:
                question_answer = QuestionAnswer(row[0], row[1], row[2], row[3], row[4])  
                question_answers.append(question_answer)

            return question_answers
        except Exception as ex:
            raise Exception("Error in getting question answers from the data store.") from ex        


# Debug Code
if __name__ == "__main__":
    datastoreManager = DataStoreManager()
    categories = datastoreManager.get_categories()
    for category in categories:        
        print ("Category: ", category.id,  ", ", category.name, ", ", category.description, ", ", category.group)        

        questions = datastoreManager.get_questions(category.id)
        for question in questions:
            print ("Question: ", question.id,  ", ", question.text,  ", ", question.description,  ", ", question.max_points, ", ", question.category_id)
        
            question_answers = datastoreManager.get_question_answers(question.id)
            for question_answer in question_answers:
                print ("QuestionAnswer: ", question_answer.id,  ", ", question_answer.text,  ", ", question_answer.description,  ", ", question_answer.points, ", ", question_answer.question_id)           
     