import pygame
class character():

    def __init__ (self,atk,maxatk,df,maxdf,hp,maxhp):
        self.hp=hp
        self.df=df
        self.atk=atk
        self.maxhp=maxhp
        self.maxdf=maxdf
        self.maxatk=maxatk
    def buttonlvlup(self,win):
        pygame.draw.rect(win,(255,255,255),(60,60,200,360),0)
        a=pygame.font.SysFont('幼圆',32)
        text1= a.render('hp:'+str(int(self.hp)),True,(255,0,0))
        win.blit(text1,(80,80))  

class Game():
    def __init__(self):
        self.character1=character(2500,2500,1200,1200,12500,12500)
        self.leveluppoint=40


    # def levelup(self):
        
