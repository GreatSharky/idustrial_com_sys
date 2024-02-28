from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683
path ="basic"
msg = "101"

client = HelperClient(server=(host, port))
response = client.put(path,msg)
print(response.pretty_print())
client.stop()