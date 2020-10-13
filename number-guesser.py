from flask import Flask, render_template, redirect, session, request 
import random

app = Flask(__name__)
app.secret_key = 'number guesser key'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(0,101)
        session['tries'] = 0
    print(session['number'])
    return render_template("index.html")

@app.route('/submit',methods = ['POST'])
def submit():
    session['tries'] += 1
    if int(request.form['number']) == session['number']:
        session['guess'] = 'Correct!'
    elif int(request.form['number']) > session['number']:
        session['guess'] = 'Too High!'
    else:
        session['guess'] = 'Too Low!'
    return redirect('/')
@app.route('/clear') 
def clear():
    if 'number' in session: 
        session.pop('number')
    if 'guess' in session: 
        session.pop('guess')
    if 'tries' in session: 
        session.pop('tries')
    if 'leaderboard' in session: 
        session.pop('leaderboard')
    return redirect('/')
@app.route('/reset', methods = ['POST'])
def reset():
    
    if 'leaderboard' in session:
        session['leaderboard'].append({'name':request.form['name'],'number':session['number'],'tries':session['tries']})
    else:
        session['leaderboard'] = [{'name':request.form['name'],'number':session['number'],'tries':session['tries']}]
    if 'number' in session: 
        session.pop('number')
    if 'guess' in session: 
        session.pop('guess')
    if 'tries' in session: 
        session.pop('tries')
    return redirect('/')

if __name__ == "__main__":
    app.run(port=5004,debug=True) 