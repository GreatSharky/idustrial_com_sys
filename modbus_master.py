import socket
import math

ip = "127.0.0.1"
port = 502

def create_request(trs, unit_id, function, start_address, quantity, value):
    trans_bytes = trs.to_bytes(2)
    prot_bytes = int(0).to_bytes(2)
    id_bytes = unit_id.to_bytes(1)
    fc_bytes = function.to_bytes(1)
    sa_bytes = start_address.to_bytes(2)
    if function in [1,3,4]:
        data = quantity.to_bytes(2)
    elif function in [5]:
        if value == 1:
            data = b'\xff\x00'
        else:
            data = value.to_bytes(2)
    elif function in [15,16]:
        if function in [15]:
 #           for i in range(quantity):
  #              byte_value |= (value << i)
   #         byte_length = math.ceil(quantity/8)
    #        byte_value <<= (byte_length-quantity)
     #       data = quantity.to_bytes(2) + len(byte_value.to_bytes(int(byte_length/8))).to_bytes() + byte_value.to_bytes(int(byte_length/8))
            byt_needed = math.ceil(quantity/8)
            bit_needed = byt_needed*8
            n = quantity
            val_bytes = b''
            for i in range(byt_needed):
                if n >= 8:
                    bin_str = str(value) * 8
                    n -= 8
                else:
                    bin_str = "0" * (8-n) + str(value) * n
                byt = int(bin_str, 2).to_bytes(1, byteorder='big')
                val_bytes += byt
            data = quantity.to_bytes(2) + len(val_bytes).to_bytes() + val_bytes
        else:
            data = quantity.to_bytes(2) + value.to_bytes(2)
    else:
        data = value.to_bytes(2)
    pdu = fc_bytes + sa_bytes + data + id_bytes
    length_bytes = len(pdu).to_bytes(2)
    return trans_bytes + prot_bytes +length_bytes + id_bytes + fc_bytes + sa_bytes + data

def create_byte_from_inputs(inputs, value):
    byte_value = 0
    for i in range(inputs):
        byte_value |= (value << i)
    return byte_value

def wireshark1(response):
    placeholder = []
    output = {
        'Transaction Identifier': 0,
        'Protocol Identifier': 0,
        'Length': 0, 
        'Unit Identifier': 0, 
        'Function Code': 1, 
        'Byte Count': 0, 
        'Data': []
    }
    for i, byt in enumerate(response):
        if i % 2 == 0  and i != 6 and i != 8:
            placeholder.append(response[i:i+2])
        elif i == 6:
            placeholder.append(response[i])
        elif i == 7:
            placeholder.append(response[i])
        elif i == 8:
            placeholder.append(response[i])
        elif i == 9:
            placeholder.append(response[i:])

    for i, key in enumerate(output):
        if key != "Data": 
            output[key] = placeholder[i]
        else:
            output[key] = placeholder[i]
    
    for key in output:
        if type(output[key]) == int:
            print(f"{key} : {output[key]}")
        elif type(output[key]) == bytes:
            if key == "Data":
                n = 0
                for byte in output[key]:
                    for i in range(8):
                        bit = (byte >> i) & 1
                        print(f"{n} : {bit}")
                        n += 1
            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))

def wireshark2(response):
    placeholder = []
    output = {
        'Transaction Identifier': 0,
        'Protocol Identifier': 0,
        'Length': 0, 
        'Unit Identifier': 0, 
        'Function Code': 1, 
        'Byte Count': 0, 
        'Data': []
    }
    for i, byt in enumerate(response):
        if i % 2 == 0  and i != 6 and i != 8:
            placeholder.append(response[i:i+2])
        elif i == 6:
            placeholder.append(response[i])
        elif i == 7:
            placeholder.append(response[i])
        elif i == 8:
            placeholder.append(response[i])
        elif i == 9:
            placeholder.append(response[i:])

    for i, key in enumerate(output):
        if key != "Data": 
            output[key] = placeholder[i]
        else:
            output[key] = placeholder[i]
    
    for key in output:
        if type(output[key]) == int:
            print(f"{key} : {output[key]}")
        elif type(output[key]) == bytes:
            if key == "Data":
                for byte in output[key]:
                    print(f"Coil : {byte}")
            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))

def wireshark3(response):
    placeholder = []
    output = {
        'Transaction Identifier': 0,
        'Protocol Identifier': 0,
        'Length': 0, 
        'Unit Identifier': 0, 
        'Function Code': 1, 
        'Byte Count': 0, 
        'Data': []
    }
    for i, byt in enumerate(response):
        if i % 2 == 0  and i != 6 and i != 8:
            placeholder.append(response[i:i+2])
        elif i == 6:
            placeholder.append(response[i])
        elif i == 7:
            placeholder.append(response[i])
        elif i == 8:
            placeholder.append(response[i])
        elif i == 9:
            placeholder.append(response[i:])
            break

    for i, key in enumerate(output):
        if key != "Data": 
            output[key] = placeholder[i]
        else:
            output[key] = placeholder[i]
    
    for key in output:
        if type(output[key]) == int:
            print(f"{key} : {output[key]}")
        elif type(output[key]) == bytes:
            if key == "Data":
                byte_array = output[key]
                n = 0
                for i in range(0, len(byte_array), 2):
                    # Combine the high byte and the low byte to form the integer
                    high_byte = byte_array[i]
                    low_byte = byte_array[i + 1]
                    integer_value = (high_byte << 8) | low_byte
                    print(f"Register {n} : {integer_value}")
                    n += 1

            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))

def wireshark4(response):
    placeholder = []
    output = {
        'Transaction Identifier': 0,
        'Protocol Identifier': 0,
        'Length': 0, 
        'Unit Identifier': 0, 
        'Function Code': 1, 
        'Byte Count': 0, 
        'Data': []
    }
    for i, byt in enumerate(response):
        if i % 2 == 0  and i != 6 and i != 8:
            placeholder.append(response[i:i+2])
        elif i == 6:
            placeholder.append(response[i])
        elif i == 7:
            placeholder.append(response[i])
        elif i == 8:
            placeholder.append(response[i])
        elif i == 9:
            placeholder.append(response[i:])
            break

    for i, key in enumerate(output):
        if key != "Data": 
            output[key] = placeholder[i]
        else:
            output[key] = placeholder[i]
    
    for key in output:
        if type(output[key]) == int:
            print(f"{key} : {output[key]}")
        elif type(output[key]) == bytes:
            if key == "Data":
                byte_array = output[key]
                n = 0
                for i in range(0, len(byte_array), 2):
                    # Combine the high byte and the low byte to form the integer
                    high_byte = byte_array[i]
                    low_byte = byte_array[i + 1]
                    integer_value = (high_byte << 8) | low_byte
                    print(f"Register {n} : {integer_value}")
                    n += 1

            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))

def wireshark5(response):
    placeholder = []
    output = {
        'Transaction Identifier': 0,
        'Protocol Identifier': 0,
        'Length': 0, 
        'Unit Identifier': 0, 
        'Function Code': 1, 

    }
    for i, byt in enumerate(response):
        if i % 2 == 0  and i != 6 and i != 8:
            placeholder.append(response[i:i+2])
        elif i == 6:
            placeholder.append(response[i])
        elif i == 7:
            placeholder.append(response[i])
        elif i == 8:
            placeholder.append(response[i])
        elif i == 9:
            placeholder.append(response[i:])
            break

    for i, key in enumerate(output):
        if key != "Data": 
            output[key] = placeholder[i]
        else:
            output[key] = placeholder[i]
    
    for key in output:
        if type(output[key]) == int:
            print(f"{key} : {output[key]}")
        elif type(output[key]) == bytes:
            if key == "Data":
                byte_array = output[key]


            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))

def wireshark6(response):
    placeholder = []
    output = {
        'Transaction Identifier': 0,
        'Protocol Identifier': 0,
        'Length': 0, 
        'Unit Identifier': 0, 
        'Function Code': 1, 
        'Data': []
    }
    for i, byt in enumerate(response):
        if i % 2 == 0  and i != 6 and i != 8:
            placeholder.append(response[i:i+2])
        elif i == 6:
            placeholder.append(response[i])
        elif i == 7:
            placeholder.append(response[i])
        elif i == 8:
            placeholder.append(response[i:])


    for i, key in enumerate(output):
        if key != "Data": 
            output[key] = placeholder[i]
        else:
            output[key] = placeholder[i]
    
    for key in output:
        if type(output[key]) == int:
            print(f"{key} : {output[key]}")
        elif type(output[key]) == bytes:
            if key == "Data":
                print("Data : {}".format(int.from_bytes(output[key], byteorder="big")))


            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))

def wireshark15(response):
    placeholder = []
    output = {
        'Transaction Identifier': 0,
        'Protocol Identifier': 0,
        'Length': 0, 
        'Unit Identifier': 0, 
        'Function Code': 1, 
        'Reference': 0, 
        'Bit count': 0
    }
    for i, byt in enumerate(response):
        if i % 2 == 0  and i != 6:
            placeholder.append(response[i:i+2])
        elif i == 6:
            placeholder.append(response[i])
        elif i == 7:
            placeholder.append(response[i])


    for i, key in enumerate(output):
        output[key] = placeholder[i]
    
    for key in output:
        if type(output[key]) == int:
            print(f"{key} : {output[key]}")
        elif type(output[key]) == bytes:
            if key == "Data":
                n = 0
                for byte in output[key]:
                    for i in range(8):
                        bit = (byte >> i) & 1
                        print(f"{n} : {bit}")
                        n += 1
            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))

def analysis(output):
    print(output)
    for key in output:
        if type(output[key]) == int:
            print("{} : {}".format(key, output[key]))
        elif type(output[key]) == bytes:
            if key == "Data":
                for j in range(8):
                    bit = (output[key] >> j) & 1
                    print(bit, end=" ")
            else:
                print("{} : {}".format(key, int.from_bytes(output[key], "big")))
        else:
            if output["Function Code"] != 1:
                for i, byt in enumerate(output[key]):
                    print("Register value {} = {}".format(i, int.from_bytes(byt, "big")))
            else:
                for i in output["Data"]:
                    for j in range(8):
                        bit = (i >> j) & 1
                        print(bit, end=" ")


def main():
    tx = 68
    id = 1
    function_code = input("Provide Function Code: ")
    print("Selected code: ", function_code)
    function_code = int(function_code)
    address = input("Provide Address: ")
    print("Selected address: ", address)
    address = int(address)
    quantity = input("Provide Quantity Of Registers/Coils: ")
    print("Selected quantity: ", quantity)
    quantity = int(quantity)
    value = input("Provide Value: ")
    print("Selected value: ", value)
    value = int(value)

    request = create_request(tx, id, function_code,address,quantity,value)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((ip,port))
        soc.sendall(request)
        res = soc.recv(9000000)
        tx += 1
    print("Request",request)
    print("Response", res)
    if res[7] == 1:
        output = wireshark1(res)
    elif res[7] == 2:
        output = wireshark2(res)
    elif res[7] == 3:
        output = wireshark3(res)
    elif res[7] == 4:
        output = wireshark4(res)
    elif res[7] == 5:
        wireshark5(res)
    elif res[7] == 6:
        wireshark6(res)
    elif res[7] == 15:
        wireshark15(res)

    #analysis(output)

main()