# 142103005 Pallavi Gaikwad
import socket

def server():
    host=socket.gethostname()
    ipofhost=socket.gethostbyname(host)
    port=4002
    print("IP of server: ",ipofhost,"\nPort: ",port)

    server=socket.socket()
    server.bind((host,port))

    server.listen(1)
    conn,addr=server.accept()
    print("\nClient is connected to server from :"+ str(addr))
    
    while True:

        data=conn.recv(1024).decode()
        if not data:
            break

        print("Message From Client:"+str(data))
        data=input('Message To client: ')
        conn.send(data.encode())

    conn.close()


server()