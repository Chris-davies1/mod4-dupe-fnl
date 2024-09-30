from flask import render_template, request, redirect, url_for, flash
from . import app

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/products')
def products():
    return render_template('Products.html')

@app.route('/happy_customers')
def happy_customers():
    return render_template('Happy Customers.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        comments = request.form['comments']
        # Process the form data (e.g., save to database, send email, etc.)
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')