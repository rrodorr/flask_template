from flask import Flask, render_template, url_for, request

app = Flask(__name__)

TITLE = 'My flask app'

# LANDING PAGE
@app.route('/')
def home():
    
    section_title = 'Welcome'
    # The context dict is required (but can be empty)
    context = {
        'subtitle': section_title,
        'header_h1': section_title
    }

    return render_template('index.html', title=TITLE, context=context)

# This enables running the app without environment vars set (simply using `python application.py` instead of `flask run`)
if __name__ == '__main__':
    app.run(debug=True)