class character:
    def __init__(self,maxatk,atk,df,maxdf,hp,maxhp,speed,crit,crit_damage):
        self.atk=atk
        self.maxatk=maxatk
        self.df=df
        self.maxdf=maxdf
        self.hp=hp
        self.maxhp=maxhp
        self.speed=speed
        self.crit=crit
        self.crit_damange=crit_damage
class truecharacter:
    def __init__(self):
        self.anjerika1=character(1200,1200,1400,1400,25000,25000,220,0.15,1.5)
        self.ran1=character(2400,2400,900,900,9500,9500,300,0.35,2)
        self.anjerika2=character(1200,1200,1400,1400,25000,25000,220,0.15,1.5)
        self.ran2=character(2400,2400,900,900,9500,9500,300,0.35,2)

        self.list_playerone=[self.anjerika1,self.ran1]
        self.list_playertwo=[self.anjerika2,self.ran2]

        self.listplayer=[self.list_playerone,self.list_playertwo]