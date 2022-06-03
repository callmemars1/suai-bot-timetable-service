import grpc

import TimeTableService_pb2
import TimeTableService_pb2_grpc
import logging


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = TimeTableService_pb2_grpc.TimetableProviderStub(channel)
        response = stub.GetTimetable(TimeTableService_pb2.TimetableRequest(group='5031'))
        print(f'{response.actualWeekType=}')
        for lesson in response.lessons:
            print(f'{lesson.groups=}\n',
                  f'{lesson.teachers=}\n',
                  f'{lesson.building=}\n',
                  f'{lesson.classRooms=}\n',
                  f'{lesson.weekDay=}\n',
                  f'{lesson.weekTypes=}\n',
                  f'{lesson.type=}\n',
                  f'{lesson.name=}\n',
                  f'{lesson.startTime=}\n',
                  f'{lesson.endTime=}\n',
                  f'{lesson.orderNumber=}\n')


if __name__ == '__main__':
    logging.basicConfig()
    run()
