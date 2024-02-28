import socket

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
    elif function in [15,16]:
        data = quantity.to_bytes(2) + value.to_bytes(2)
    else:
        data = value.to_bytes(2)
    pdu = fc_bytes + sa_bytes + data + id_bytes
    length_bytes = len(pdu).to_bytes(2)
    return trans_bytes + prot_bytes +length_bytes + id_bytes + fc_bytes + sa_bytes + data

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
            output[key] = [placeholder[i]]
    
    return output

def analysis(output):
    print(output)
    for key in output:
        if type(output[key]) == int:
            print("{} : {}".format(key, output[key]))
        elif type(output[key]) == bytes:
            print("{} : {}".format(key, int.from_bytes(output[key], "big")))
        else:
            if output["Function Code"] != 1:
                for i, byt in enumerate(output[key]):
                    print("Register value {} = {}".format(i, int.from_bytes(byt, "big")))
            else:
                for i in output["Data"]:
                    print("Register value {} = {}".format("liiba", i))



def main():
    tx = 2
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
    analysis(output)

main()