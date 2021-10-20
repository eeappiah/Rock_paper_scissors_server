import socket
from _thread import *
from player import Player
import pickle

server = "192.168.1.74"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started")


players = [Player(0,0,50,50,(255,0,0)), Player(0,0,50,50,(0,255,0))]


def thread_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(thread_client, (conn, currentPlayer))
    currentPlayer += 1
