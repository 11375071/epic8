import socket
from _thread import *
import pickle
from game import Game

server = "183.172.132.113"
port = 5555
print(server)
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
                    
                    if data == "get":
                        pass
                        
                    if data[-5:] == "95559":
                        player, id, lv, k = data.split('I')
                        player, id, lv = int(player), int(id), int(lv)
                        game.up_lv(player, id, lv)
                        game.point_consume(player,id,lv)
                    
                    if data[-5:] == "75884":
                        player, id, lv, num, k = data.split('I')
                        player, id, lv, num = int(player), int(id), int(lv), int(num)
                        game.extra_up(player, id, lv, num)

                    if data[-5:] == "36912":
                        print(data)
                        player, id, lv, k = data.split('I')
                        player, id, lv = int(player), int(id), int(lv)
                        game.reset(player, id, lv)
                    
                    if data[-5:] == "65536":
                        print(data)
                        player, id, lv, k = data.split('I')
                        player, id, lv = int(player), int(id), int(lv)
                        game.skill_points(player, id, lv)

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