import pygame
from network import Network
import pickle
from game import Game
pygame.font.init()

width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class character():
    def __init__ (self,hp,atk,df,maxhp,maxatk,maxdf):
        self.hp=hp
        self.df=df
        self.atk=atk
        self.maxhp=maxhp
        self.maxdf=maxdf
        self.maxatk=maxatk

def redrawWindow(win, game, player):
    win.fill((128,128,128))
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        if player == 0:
            pygame.draw.rect(win,(255,255,255),(60,60,200,360),0)
            a=pygame.font.SysFont('幼圆',32)
            text1= a.render('hp:'+str(int(game.hp1)),True,(255,0,0))
            win.blit(text1,(80,80))

            pygame.draw.rect(win,(255,255,255),(560,60,200,360),0)
            text1= a.render('hp:'+str(int(game.hp2)),True,(255,0,0))
            win.blit(text1,(580,80))
        if player == 1:
            pygame.draw.rect(win,(255,255,255),(60,60,200,360),0)
            a=pygame.font.SysFont('幼圆',32)
            text1= a.render('hp:'+str(int(game.hp2)),True,(255,0,0))
            win.blit(text1,(80,80))

            pygame.draw.rect(win,(255,255,255),(560,60,200,360),0)
            text1= a.render('hp:'+str(int(game.hp1)),True,(255,0,0))
            win.blit(text1,(580,80))
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    # gamestart = Game()

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, (255,0,0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255,0,0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # pos = pygame.mouse.get_pos()
                # for btn in btns:
                #     if btn.click(pos) and game.connected():
                #         if player == 0:
                #             if not game.p1Went:
                #                 n.send(btn.text)
                #         else:
                #             if not game.p2Went:
                #                 n.send(btn.text)
                x,y=event.pos
                if 60<=x<=260 and 60<=y<=420:
                    if player == 0:
                        n.send("p1+1")
                    if player == 1:
                        n.send("p2+1")

        redrawWindow(win, game, player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()