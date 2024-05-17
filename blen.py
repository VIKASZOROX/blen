# blen.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/home.html')
def index():
    return render_template('home.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/books')
@app.route('/books.html')
def books():
    return render_template('books.html')

# Error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
