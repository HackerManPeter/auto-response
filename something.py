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
