# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(os.path.dirname(argv[0]))
sys.path.insert(0, root_path)

from flask import Flask, request, jsonify
from flask_cors import CORS
from constants import Constants
from app import App


# Start server
server_app = Flask(__name__)
CORS(server_app)  # Enable CORS for AJAX requests
app = App()


# Routes
# Version route
@server_app.route("/version", methods=["GET"])
def version():    
    return jsonify({"response": Constants.VERSION})


# Get categories
@server_app.route("/categories", methods=["GET"])
def get_categories():
    return app.question_manager.get_categories()        

    # Get category with details
    def get_category_with_details(self, category_id):
        return App.question_manager.get_category_with_details(category_id)
  
    # Start user session
    def start_user_session(self, user_name):
        App.session_manager.start_user_session(user_name)

    # End user session
    def end_user_session(self, user_name):
        App.session_manager.end_user_session(user_name)

    # Update user question response
    def update_user_question_response(self, user_name, category_id, question_id, question_answer_id):  
        category_with_details = self.question_manager.get_category_with_details(category_id)      
        App.session_manager.update_user_question_response(user_name, category_id, category_with_details.name, question_id, question_answer_id)

    # Get user sustainability score
    def get_user_sustainability_score(self, user_name):  
        return App.calculator.calculate_sustainability_score(App.session_manager.get_user_session(user_name))
  

# Debug Code
if __name__ == "__main__":
    server_app.run(debug=True)
