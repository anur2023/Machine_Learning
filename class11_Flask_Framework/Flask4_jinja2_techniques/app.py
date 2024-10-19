from flask import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/success/<int:score>')
def sucess_score(score):
    res = "Passed" if score >= 50 else "Failed"
    exp = {'score': score, "Status": res}
    return render_template('result.html', exp=exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('resultif.html', result=score)

@app.route('/submit', methods=['POST', 'GET'])
def get_result():
    if request.method == 'POST':
        science = int(request.form['science'])
        maths = int(request.form['maths'])
        data_science = int(request.form['datascience'])
        java = int(request.form['java'])
        
        total_average_result = (science + maths + data_science + java) / 4
        
        return redirect(url_for('successif', score=total_average_result))
    
    return render_template('form.html')  

if __name__ == "__main__":
    app.run(debug=True)
