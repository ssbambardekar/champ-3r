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
    categories = app.question_manager.get_categories()

    categories_json = []
    for category in categories:
        categories_json.append(category.toJson())
    
    return jsonify({"response": categories_json})


# Get category with details
@server_app.route("/category/<category_id>", methods=["GET"])
def get_category_with_details(category_id):
    category_with_details = app.question_manager.get_category_with_details(category_id)

    category_with_details_json = category_with_details.toJson()

    return jsonify({"response": category_with_details_json})


# Start user session
@server_app.route("/login", methods=["POST"])
def start_user_session():
    request_data = request.get_json()
    user_name = request_data["user_name"]
    app.session_manager.start_user_session(user_name)

    return jsonify(success=True)


# End user session
@server_app.route("/logout", methods=["PUT"])
def end_user_session():
    request_data = request.get_json()
    user_name = request_data["user_name"]
    app.session_manager.end_user_session(user_name)

    return jsonify(success=True)


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
