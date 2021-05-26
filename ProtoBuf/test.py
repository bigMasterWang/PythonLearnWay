# coding=utf-8
from MessageTest_pb2 import SearchRequest

test = SearchRequest()

test.query = 'hello world'
test.page_number = 1
test.result_per_page = 2

bytes = test.SerializeToString()
result = SearchRequest()
result.ParseFromString(bytes)

print result.query


from test_pb2 import TestMsg

send_msg = TestMsg()
send_msg.name = '你妈必死'

send_bytes = send_msg.SerializeToString()
print send_bytes, len(send_bytes)
recv_msg = TestMsg()
recv_msg.ParseFromString(send_bytes)
print recv_msg.name