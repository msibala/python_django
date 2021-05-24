from flask import Flask, render_template
from werkzeug.datastructures import CombinedMultiDict  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__) 
        
@app.route('/')       
def tresbox():
    return render_template("checkers.html" )


def dogs():
    return "dogs"


if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
