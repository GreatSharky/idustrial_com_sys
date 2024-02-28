import socket

direction = input("give direction: ")
up_packet = ""
down_packet = ""
left_packet = '202d5461726765744e616d6520224d433022202d506172616d73202022545f524f4231222c222f4d6f64756c65312f506174685f32302f4d6f76654c2f31363022'
right_packet = ""
dest_port = 5515
dest_ip = "192.168.125.1"
dest_mask = ""

packet = ""
if direction == "right":
    packet = right_packet
elif direction == "up":
    packet = up_packet
elif direction == "down":
    packet = down_packet
elif direction == "left":
    packet = left_packet

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((dest_ip,dest_port))
    s.send(packet)