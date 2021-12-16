import requests
class Form:
    def __init__(self, API_TOKEN, FORM_ID):
        self.API_TOKEN = API_TOKEN
        self.FORM_ID = FORM_ID

    def __sort_answers(self, answers) -> list:
        '''Returns a list of dictionaries where each key is a question ID 
            and the value is the users answer'''
        database = list()

        for i in range(len(answers)):
            record = dict()
            user = answers[i]
            for j in range(len(user['answers'])):
                question = user['answers'][j]
                record[question['field']['id']] = question[list(question.keys())[-1]]
            database.append(record)

        return database

    def get_answers(self, **query_params) -> list:
        '''Returns a list of dictionaries where each key is a question ID 
            and the value is the users answer'''

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

        answers = response.json()['items']

        data = self.__sort_answers(answers)

        return data

    