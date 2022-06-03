import loguru
from pymongo import MongoClient


class RaspMongoClient:
    @loguru.logger.catch
    def __init__(self, connection_string: str, database: str, collection: str):
        try:
            loguru.logger.info('start connecting to bd')
            self.client = MongoClient(connection_string)
            loguru.logger.info('connected to bd')
        except Exception as _ex:
            loguru.logger.warning('connection with mangoDB failed')
            loguru.logger.warning(_ex)
        self.database = self.client[database]
        self.collection = self.client[database][collection]

    @loguru.logger.catch
    def disconnect(self):
        self.client.close()
        loguru.logger.info('disconnect from bd')

    @loguru.logger.catch
    def insert_document(self, collection, data):
        return self.database[collection].insert_one(data)

    def add_lessons(self, lessons: list):
        self.collection.insert_many(lessons)

    def add_lesson(self, lesson: dict):
        self.collection.insert_one(lesson)

    @loguru.logger.catch
    def find_document(self, elements, collection, multiple=True):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        if multiple:
            results = self.database[collection].find(elements)
            return [r for r in results]
        else:
            return self.database[collection].find_one(elements)
