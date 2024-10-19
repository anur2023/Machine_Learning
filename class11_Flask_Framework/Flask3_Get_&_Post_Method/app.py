from flask import *

app  = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/form',methods=['GET','POST'])
def get_post_request():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)