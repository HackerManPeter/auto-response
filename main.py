import os
import time

import schedule
from form import Form
from pymongo import MongoClient
from dotenv import load_dotenv

def repopulate_database(collection, form_object):
    try:
        collection.delete_many({})
        print('Successfully Deleted')
    except Exception as err:
        print(err)

    all_entries = form_object.get_answers(page_size=1000, completed=True)
    
    try:
        collection.insert_many(all_entries)
        print('Succesfully Updated')
    except Exception as err:
        print(err)


def get_new_entries(collection, form_object, difference):
    response_cursor = collection.find({}).sort('$natural', -1).limit(difference + 1)
    last_response = list(response_cursor)[0]
    new_entries = form_object.get_answers(completed=True, after=last_response['token'], page_size=1000)
    return new_entries

    

def main():
    load_dotenv()

    CONNECTION_STRING = os.environ['CONNECTION_STRING']
    client = MongoClient(CONNECTION_STRING)
    collection = client.gdsc.members

    API_TOKEN = os.environ['API_TOKEN']
    FORM_ID = os.environ['FORM_ID']
    form = Form(API_TOKEN, FORM_ID)

    typeform_entries = form.total_items
    database_entries = collection.estimated_document_count()

    if database_entries < typeform_entries:
        difference = typeform_entries - database_entries
        new_entries = get_new_entries(collection, form, difference)
        try:
            collection.insert_many(new_entries)
            print("Successfully Updated")
            return
        except Exception as err:
            print(err)
            SystemExit(0)
    print("No new updates")

if __name__ == '__main__':
    schedule.every(5).seconds.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)