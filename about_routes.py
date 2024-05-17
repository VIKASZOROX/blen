from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
