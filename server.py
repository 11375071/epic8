import socket
from _thread import *
import pickle
from game import Game

server = "183.172.134.98"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:

                    if data == "0anj_atk":
                        game.up_atk(0, 0)
                    elif data == "1anj_atk":
                        game.up_atk(1, 0) 
                    elif data == "0lan_atk":
                        game.up_atk(0, 1)
                    elif data == "1lan_atk":
                        game.up_atk(1, 1) 
                    if data == "0anj_hp":
                        game.up_hp(0, 0)
                    elif data == "1anj_hp":
                        game.up_hp(1, 0) 
                    elif data == "0lan_hp":
                        game.up_hp(0, 1)
                    elif data == "1lan_hp":
                        game.up_hp(1, 1) 
                    

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))