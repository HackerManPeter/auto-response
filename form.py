import requests
class Form:
    def __init__(self, API_TOKEN, FORM_ID):
        self.API_TOKEN = API_TOKEN
        self.FORM_ID = FORM_ID

        url = f'https://api.typeform.com/forms/{self.FORM_ID}/responses'
        headers = {'Authorization': f'Bearer {self.API_TOKEN}'}

        try:
            self.__response = requests.get(url, headers=headers)
            if self.__response.raise_for_status():
                quit()
        except requests.exceptions.RequestException as e:
            raise(e)

        self.page_count = self.__response.json()['page_count']
        self.total_items = self.__response.json()['total_items']


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

    def get_question_ids(self):
        ids = list()
        question_ids = self.__response.json()['items'][0]['answers']

        for question_number in range(len(question_ids)):
            question_ids[question_number]['field']['id']

        return ids

        


if __name__ == '__main__':
    import os
    import json

    from dotenv import load_dotenv
    load_dotenv()

    API_TOKEN = os.environ['FORM_TOKEN']
    FORM_ID = os.environ['FORM_ID']
    
    response = Form(API_TOKEN, FORM_ID)

    response.get_question_ids()