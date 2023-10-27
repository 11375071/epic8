import pygame
from network import Network
import pickle
import script
from game import Game
pygame.font.init()

width = 1280
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 50

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

def redrawWindow(window, game, player):
    window.fill((128,128,128))
    a=pygame.font.SysFont('幼圆',32)
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        if player == 0:
            for i in range(2):
                pygame.draw.rect(window,(255,255,255),(60+250*i,60,200,360),0)
                text0 = a.render('hp:'+str(int(game.AA.listplayer[0][i].hp)),True,(255,0,0))
                window.blit(text0,(80+250*i,80))
                text0 = a.render('atk:'+str(int(game.AA.listplayer[0][i].atk)),True,(255,0,0))
                window.blit(text0,(80+250*i,180))
            text0 = a.render('pt:'+str(int(game.pt0)),True,(255,0,0))
            window.blit(text0,(80+150*i,80))
        if player == 1:
            for i in range(2):
                pygame.draw.rect(window,(255,255,255),(60+250*i,60,200,360),0)
                text1 = a.render('hp:'+str(int(game.AA.listplayer[1][i].hp)),True,(255,0,0))
                window.blit(text1,(80+250*i,80))
                text0 = a.render('atk:'+str(int(game.AA.listplayer[1][i].atk)),True,(255,0,0))
                window.blit(text0,(80+250*i,180))
            text0 = a.render('pt:'+str(int(game.pt1)),True,(255,0,0))
            window.blit(text0,(80+150*i,80))
        for btn in btns:
            btn.draw(window)
    pygame.display.update()

btns = [Button("anj_atk", 50, 500, (255,0,0)), Button("anj_hp", 220, 500, (255,0,0)), Button("lan_atk", 390, 500, (255,0,0)), Button("lan_hp", 560, 500, (255,0,0))]
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
            game = n.send("get")                             ############
        except:
            run = False
            print("Couldn't get game")
            break

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        n.send(str(player)+btn.text)
                # x,y = pos
                # if 60<=x<=260 and 60<=y<=420:
                #     if player == 0:
                #         n.send("anjerikaA+1级")

                #     if player == 1:
                #         n.send("anjerikaB+1级")

                # if 310<=x<=510 and 60<=y<=420:
                #     if player == 0:
                #         n.send("ranA+1级")

                #     if player == 1:
                #         n.send("ranB+1级")

                    

        redrawWindow(window, game, player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        window.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        window.blit(text, (100,200))
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