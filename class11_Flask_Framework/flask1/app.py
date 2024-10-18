from flask import Flask
'''
It will create an instance of the flask class which will be your web server gateway interface.
'''
app = Flask(__name__)
@app.route("/")
def welcome():
    return "This is a welcome page"

@app.route('/index')
def index():
    return "This is an index page"

if __name__ == "__main__":
    app.run(debug=True)