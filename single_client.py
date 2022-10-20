#142103005 Pallavi Gaikwad

import socket

def client(ip,port):

    ip=input("Enter the IP of the server: ")
    port=int(input("Enter the port of the server: "))
    client=socket.socket()
    client.connect((ip,port))
    message=input("Message To server: ")

    while True:

      if(message=='thanks'):
        break

      client.send(message.encode())
      data=client.recv(1024).decode()
      print("Message From server: "+data)
      message=input("Message To server: ")

    client.close()

client("127.0.1.1",4002)