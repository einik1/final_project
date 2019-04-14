import socket
import select
import msvcrt


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.56.1', 4444))
finish = True

while finish:
    rlist, wlist, xlist = select.select([client_socket], [], [])
    for current_client in rlist:
        data = current_client.recv(1024)
        print "the server sent: " + data + "\n"
    client_data = msvcrt.getch()
    client_socket.send(client_data)
    if client_data == "exit":
        finish = False

client_socket.close()




