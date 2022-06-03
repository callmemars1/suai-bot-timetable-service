# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TimeTableService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16TimeTableService.proto\x12\rSuaiTimetable\"W\n\x10TimetableRequest\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07teacher\x18\x02 \x01(\t\x12\x10\n\x08\x62uilding\x18\x03 \x01(\t\x12\x11\n\tclassRoom\x18\x04 \x01(\t\"P\n\x0eTimetableReply\x12&\n\x07lessons\x18\x01 \x03(\x0b\x32\x15.SuaiTimetable.Lesson\x12\x16\n\x0e\x61\x63tualWeekType\x18\x02 \x01(\t\"\xc9\x01\n\x06Lesson\x12\x0e\n\x06groups\x18\x01 \x03(\t\x12\x10\n\x08teachers\x18\x02 \x03(\t\x12\x10\n\x08\x62uilding\x18\x03 \x01(\t\x12\x12\n\nclassRooms\x18\x04 \x03(\t\x12\x0f\n\x07weekDay\x18\x05 \x01(\t\x12\x11\n\tweekTypes\x18\x06 \x03(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x11\n\tstartTime\x18\t \x01(\t\x12\x0f\n\x07\x65ndTime\x18\n \x01(\t\x12\x13\n\x0borderNumber\x18\x0b \x01(\t2c\n\x11TimetableProvider\x12N\n\x0cGetTimetable\x12\x1f.SuaiTimetable.TimetableRequest\x1a\x1d.SuaiTimetable.TimetableReplyB\x1b\xaa\x02\x18Suai.Bot.Timetable.Protob\x06proto3')



_TIMETABLEREQUEST = DESCRIPTOR.message_types_by_name['TimetableRequest']
_TIMETABLEREPLY = DESCRIPTOR.message_types_by_name['TimetableReply']
_LESSON = DESCRIPTOR.message_types_by_name['Lesson']
TimetableRequest = _reflection.GeneratedProtocolMessageType('TimetableRequest', (_message.Message,), {
  'DESCRIPTOR' : _TIMETABLEREQUEST,
  '__module__' : 'TimeTableService_pb2'
  # @@protoc_insertion_point(class_scope:SuaiTimetable.TimetableRequest)
  })
_sym_db.RegisterMessage(TimetableRequest)

TimetableReply = _reflection.GeneratedProtocolMessageType('TimetableReply', (_message.Message,), {
  'DESCRIPTOR' : _TIMETABLEREPLY,
  '__module__' : 'TimeTableService_pb2'
  # @@protoc_insertion_point(class_scope:SuaiTimetable.TimetableReply)
  })
_sym_db.RegisterMessage(TimetableReply)

Lesson = _reflection.GeneratedProtocolMessageType('Lesson', (_message.Message,), {
  'DESCRIPTOR' : _LESSON,
  '__module__' : 'TimeTableService_pb2'
  # @@protoc_insertion_point(class_scope:SuaiTimetable.Lesson)
  })
_sym_db.RegisterMessage(Lesson)

_TIMETABLEPROVIDER = DESCRIPTOR.services_by_name['TimetableProvider']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\030Suai.Bot.Timetable.Proto'
  _TIMETABLEREQUEST._serialized_start=41
  _TIMETABLEREQUEST._serialized_end=128
  _TIMETABLEREPLY._serialized_start=130
  _TIMETABLEREPLY._serialized_end=210
  _LESSON._serialized_start=213
  _LESSON._serialized_end=414
  _TIMETABLEPROVIDER._serialized_start=416
  _TIMETABLEPROVIDER._serialized_end=515
# @@protoc_insertion_point(module_scope)