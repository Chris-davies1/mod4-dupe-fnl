#file used to create the app instance
from flask import Flask


# defines the create_app function that creates the app instance
def create_app():
    app = Flask(__name__)
    return app
