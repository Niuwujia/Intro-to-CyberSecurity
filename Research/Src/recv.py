import socket
import pickle

host = '114.214.240.179'
port = 23000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("等待连接...")
conn, addr = s.accept()
print("已连接:", addr)
data_bytes = conn.recv(1024)

data_list = pickle.loads(data_bytes)

print("接收到的数据:", data_list)

conn.close()
