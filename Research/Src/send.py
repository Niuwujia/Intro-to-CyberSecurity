import socket
import pickle

host = '114.214.225.65'
port = 23001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data_list = [1, 2, 3, 4, 5]

data_bytes = pickle.dumps(data_list)

s.sendall(data_bytes)

s.close()
