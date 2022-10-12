import random
from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = "numbers561are987key0192"  # Change the secret key so each assignment is unique.

@app.route('/')
def random_num():
    session['random'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_guess():
    guess = int(request.form['user_guess'])
    if session['random'] < guess:
        session['result'] = 'High'
        return redirect('/guess')
    elif session['random'] > guess:
        session['result'] = 'Low'
        return redirect('/guess')
    elif session['random'] == guess:
        session['result'] = 'Match'
        return redirect('/guess')

@app.route('/guess')
def results():
    return render_template('index.html')

@app.route('/again')
def play_again():
    session.clear()
    return redirect('/')

if __name__== "__main__":  # lines 10 and 11 are required on all server.py files and will not run without them.
    app.run(debug=True)

# For macs, remember to add port = 5001 << something like this check the platform