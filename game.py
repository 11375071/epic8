import script
# from client0 import num1,num0

class Game:
    def __init__(self,id):
        self.ready = False
        self.id = id
        self.AA = script.truecharacter()
        self.num0 = -1
        self.num1 = -1
        self.pt0 = 40
        self.pt1 = 40

    def up_hp(self, player, id): 
        if player == 0:
            if self.pt0:
                self.AA.listplayer[0][id].hp+=self.AA.listplayer[0][id].maxhp*0.01
                self.pt0 -= 1
        if player == 1:
            if self.pt1:
                self.AA.listplayer[1][id].hp+=self.AA.listplayer[1][id].maxhp*0.01
                self.pt1 -= 1

    def up_atk(self, player, id):
        if player == 0:
            if self.pt0:
                self.AA.listplayer[0][id].atk+=self.AA.listplayer[0][id].maxatk*0.01
                self.pt0 -= 1
        if player == 1:
            if self.pt1:
                self.AA.listplayer[1][id].atk+=self.AA.listplayer[1][id].maxatk*0.01
                self.pt1 -= 1

    def connected(self):
        return self.ready