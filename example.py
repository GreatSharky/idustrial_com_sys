import socket
import binascii


IP = "192.168.125.1"
PORT = 5000
SPEED = 300
msg = f"mov_hor,{SPEED}"

#from chatgpt
def string_to_bits(string):
    # Convert string to bytes
    bytes_string = string.encode()
    # Convert bytes to hexadecimal representation
    hex_string = binascii.hexlify(bytes_string).decode()
    # Convert hexadecimal string to binary
    binary_string = bin(int(hex_string, 16))[2:].zfill(8)
    return binary_string

ver = "01"
T = "00"
TKL = "0000"
code = "00000010"
msg_id = "0000000010000000"
marker = "11111111"
payload = string_to_bits(msg)
data = f"{ver}{T}{TKL}{code}{msg_id}{marker}{payload}"
print(data)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((IP,PORT))
    soc.sendall(data)
    res = soc.recv(1024)
print(res)