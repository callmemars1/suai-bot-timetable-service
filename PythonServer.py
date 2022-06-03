import grpc

import TimeTableService_pb2
import TimeTableService_pb2_grpc
import logging

from concurrent import futures
from config import insecure_port
from config import DB_USER, DB_NAME, DB_HOST, DB_PASS, collection_name
from rasp_mongo_client import RaspMongoClient


class TimetableService(TimeTableService_pb2_grpc.TimetableProviderServicer):
    def __init__(self, database):
        self.database = database

    def GetTimetable(self, request, context):
        req_group = request.group

        results = self.database.find_document({'groups': req_group})
        lessons = []

        for result in results:
            lesson = TimeTableService_pb2.Lesson()
            lesson.groups.extend(result['groups'])
            lesson.teachers.extend(result['teachers'])
            lesson.classRooms.extend(result['class_rooms'])
            lesson.weekDay = result['week_day']
            lesson.type = result['lesson_type']
            lesson.weekTypes.extend(result['week_type'])
            lesson.name = result['lesson_name']
            lesson.building = result['building']
            lesson.startTime = result['start_time']
            lesson.endTime = result['end_time']
            lesson.orderNumber = result['lesson_number']
            lessons.append(lesson)

        return TimeTableService_pb2.TimetableReply(lessons=lessons,
                                                   actualWeekType='верхняя',
                                                   )


def serve(database):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TimeTableService_pb2_grpc.add_TimetableProviderServicer_to_server(TimetableService(database), server)
    server.add_insecure_port(insecure_port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()

    bd = RaspMongoClient(f'mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}/',
                         f'{DB_NAME}',
                         f'{collection_name}')

    serve(bd)

    bd.disconnect()
