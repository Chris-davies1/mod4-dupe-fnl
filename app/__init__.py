from flask import Flask, g
from .app_factory import create_app

app = create_app()
app.secret_key = 'your-secret'  # Replace with an environment variable
# shows the app where to look for the routes
from . import routes


