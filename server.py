import socket
from _thread import *

from game import Game

server = "192.168.1.74"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(0)
print("Waiting for connection, Server Started")

connected = set()
games = {}
idCount = 0


def thread_client(conn, player, gameId):
    pass


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(thread_client, (conn, p, gameId))
