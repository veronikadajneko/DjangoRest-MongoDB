import lorem
import names
import datetime
import random
from pymongo import MongoClient


def get_random_date():
    start_date = datetime.datetime(2017, 1, 1)
    end_date = datetime.datetime(2020, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def get_database():

    # Provide the mongodb url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://root:example@mongo:27017/mydb?authSource=admin"

    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example
    return client.library


if __name__ == "__main__":
    # Get the database
    dbname = get_database()
    collection_name = dbname.catalog_texts

    for x in range(100):
        item = {
            'textual_paragraph': lorem.paragraph(),
            'author': names.get_full_name(),
            'date': get_random_date()
        }
        # Step 3: Insert item object directly into MongoDB via insert_one
        collection_name.insert_one(item)
        # Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 100 as {1}'.format(x, collection_name.inserted_id))
    # Step 5: Tell us that you are done
    print('finished creating 100 lines')
