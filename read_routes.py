# read_routes.py

from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('home.html')

# Route for serving PDF files
@app.route('/static/pdfs/<path:filename>')
def serve_pdf(filename):
    try:
        # Ensure that the file requested is within the 'static/pdfs' directory
        if '..' in filename:
            raise FileNotFoundError
        # Send the file from the specified directory
        return send_from_directory('static/pdfs', filename)
    except FileNotFoundError:
        # If the file is not found or there's an attempt to access directories outside 'static/pdfs'
        abort(404)

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
