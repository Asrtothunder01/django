import requests
token = 'ef6a39414528893939d02b31b71fa9512a023a92'

headers ={
    'Authorization':f'Token{token}'
}

response = requests.get('127.0.0.1:8000/api/profile',headers=headers)

if response.status_code == 200:
    print('profile data',response.json())
else:
    print('Failed to retrieve profile',response.status_code,response.text)