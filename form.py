import requests
class Form:
    def __init__(self, API_TOKEN, FORM_ID):
        self.API_TOKEN = API_TOKEN
        self.FORM_ID = FORM_ID

    def get_responses(self, **query_params):
        '''Returns form responses in json format'''

        url = f'https://api.typeform.com/forms/{self.FORM_ID}/responses'
        headers = {'Authorization': f'Bearer {self.API_TOKEN}'}

        try:
            response = requests.get(url, headers=headers, params=query_params)
            if response.raise_for_status():
                quit()
        except requests.exceptions.RequestException as e:
            raise(e)
        
        self.page_count = response.json()['page_count']
        self.total_items = response.json()['total_items']

        return response.json()['items']

