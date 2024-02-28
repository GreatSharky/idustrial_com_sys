import socket

def tcp_client(ip, port, payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((ip,port))
        soc.sendall(payload)
        res = soc.recv(1024)