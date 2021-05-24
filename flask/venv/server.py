from flask import Flask, render_template
from werkzeug.datastructures import CombinedMultiDict  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__) 
         # Just for fun, print __name__ to see what it is
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.

def index():
    return render_template("index.html",phrase="hello", times=5)
    if __name__=="__main__":
        app.run(debug=True)