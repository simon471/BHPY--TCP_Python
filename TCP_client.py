import socket

target_host = "192.168.37.247"
target_port = 9999

#create a socket object
    #AF_INET saying we are going to use a standard IPv4 address or hostname
    #SOCK_STREAM indicates that this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print response
