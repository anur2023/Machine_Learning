from flask import Flask,render_template
import time
app = Flask(__name__)

@app.route('/')
def Home_page():
    return render_template("homepage.html")
@app.route('/login')
def login_page():

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)