import loguru
from pymongo import MongoClient


class RaspMongoClient:
    def __init__(self, connection_string: str, database: str, collection: str):
        try:
            self.client = MongoClient(connection_string)
        except Exception as _ex:
            loguru.logger.warning('connection with mangoDB failed')
            loguru.logger.warning(_ex)
        self.collection = self.client[database][collection]

    def disconnect(self):
        self.client.close()

    @staticmethod
    def insert_document(collection, data):
        return collection.insert_one(data)

    def add_lessons(self, lessons: list):
        self.collection.insert_many(lessons)

    def add_lesson(self, lesson: dict):
        self.collection.insert_one(lesson)

    def find_document(self, elements, multiple=True):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        if multiple:
            results = self.collection.find(elements)
            return [r for r in results]
        else:
            return self.collection.find_one(elements)
