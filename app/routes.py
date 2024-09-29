from flask import render_template
from . import app
#tells the route to render the html file
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About Us')
def about():
    return render_template('About Us.html')

@app.route('/Products')
def exam():
    return render_template('Products.html')