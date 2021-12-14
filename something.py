import os 
import json

import requests
from dotenv import load_dotenv

load_dotenv()

FORM_TOKEN = os.environ['FORM_TOKEN']
FORM_ID = os.environ['FORM_ID']

url = f'https://api.typeform.com/forms/{FORM_ID}/responses'
headers = {
    'Authorization': f'Bearer {FORM_TOKEN}'
}

payload = {
    'page_size':1000,
    'completed':True,
    'fields': [
        'I256DdpXdlcI',
        'SaQW7s1pwJc5',
        '1cS3rSE4hp6E',
        'QT3ErEp7d9T0'
    ]
}

response = requests.get(url, headers=headers, params=payload)
answers = response.json()['items']

data = list()
for response in range(len(answers)):
    responses = dict()
    user = answers[response]['answers']
    responses['first_name'] = user[0][list(user[0])[-1]]
    responses['last_name'] = user[1][list(user[1])[-1]]
    responses['email'] = user[2][list(user[2])[-1]]
    responses['phone_number'] = user[3][list(user[3])[-1]]

    data.append(responses)


content = json.dumps(data)

with open('data.json', 'w') as data:
    data.write(content)