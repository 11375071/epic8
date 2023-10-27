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

    
    

def main():
    gamestart = Game()
    
    # player = int(n.getP())
    # print("You are player", player)

    
    # try:
    #     game = n.send("get")
    # except:
    #     run = False
    #     print("Couldn't get game")
    #     break
    
    
    gamestart.character1.buttonlvlup(win)
    # n = Network()

        

def menu_screen():
    run = True
    clock = pygame.time.Clock()
    gamestart = Game()
    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
 

        

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if 60<=x<=260 and 60<=y<=420:
                    gamestart.character1.hp+=gamestart.character1.maxhp*0.01

            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

       
    
        
        
        
        gamestart.character1.buttonlvlup(win)

        pygame.display.update()


menu_screen()

#####
