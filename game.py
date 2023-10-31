import script
# from client0 import num1,num0

class Game:
    def __init__(self,id):
        self.ready = False
        self.id = id
        
        self.num0 = -1
        self.num1 = -1
        self.pt0 = 40
        self.pt1 = 40
        self.AA = script.characters()
        self.BB = script.players()
        self.point0A = 0
        self.point1A = 0
        self.point2A = 0
        self.pointplayer1 = 0
        self.point0B = 0
        self.point1B = 0
        self.point2B = 0
        self.pointplayer2 = 0
 
    def up_lv(self, player, id, lv):
        print(self.AA.listplayer[player][id].lv)
        if self.AA.listplayer[player][id].lv!=80:
            self.AA.listplayer[player][id].hp = lv*self.AA.listplayer[player][id].maxhp*0.015+self.AA.listplayer[player][id].maxhp
            self.AA.listplayer[player][id].atk = lv*self.AA.listplayer[player][id].maxatk*0.015+self.AA.listplayer[player][id].maxatk
            self.AA.listplayer[player][id].df = lv*self.AA.listplayer[player][id].maxdf*0.015+self.AA.listplayer[player][id].maxdf
            self.AA.listplayer[player][id].crit = lv*self.AA.listplayer[player][id].maxcrit*0.006+self.AA.listplayer[player][id].maxcrit
            self.AA.listplayer[player][id].crit_damage = lv*self.AA.listplayer[player][id].maxcrit_damage*0.01+self.AA.listplayer[player][id].maxcrit_damage
            self.AA.listplayer[player][id].lv = lv

    def extra_up(self, player, id, lv, num):
        if lv == 80 :
            if num == 0:
                self.AA.listplayer[player][id].atk += self.AA.listplayer[player][id].maxatk*0.08
            if num == 1:
                self.AA.listplayer[player][id].df += self.AA.listplayer[player][id].maxdf*0.08
            if num == 2:
                self.AA.listplayer[player][id].hp += self.AA.listplayer[player][id].maxhp*0.08
            if num == 3:
                self.AA.listplayer[player][id].crit += 0.1
            if num == 4:
                self.AA.listplayer[player][id].crit_damage += 0.23
            if num == 5:
                self.AA.listplayer[player][id].effect_hit += 0.2
            if num == 6:
                self.AA.listplayer[player][id].effect_defend += 0.2
            if num ==7:
                self.AA.listplayer[player][id].speed += 15
   
    def reset(self, player, id, lv):
        self.AA.listplayer[player][id].hp = self.AA.listplayer[player][id].maxhp
        self.AA.listplayer[player][id].atk = self.AA.listplayer[player][id].maxatk
        self.AA.listplayer[player][id].df = self.AA.listplayer[player][id].maxdf
        self.AA.listplayer[player][id].crit = self.AA.listplayer[player][id].maxcrit
        self.AA.listplayer[player][id].crit_damage = self.AA.listplayer[player][id].maxcrit_damage
        self.AA.listplayer[player][id].effect_hit = self.AA.listplayer[player][id].maxeffect_hit
        self.AA.listplayer[player][id].effect_defend = self.AA.listplayer[player][id].maxeffect_defend
        self.AA.listplayer[player][id].lv = 0

    def point_consume(self, player, id, lv):
        if player == 0:
            if id == 0:
                s = 0
                for i in range(lv):
                    s+= 1.025**i
                self.point0A = s
            if id == 1:
                s = 0
                for i in range(lv):
                    s+= 1.025**i
                self.point1A = s
            if id == 2:
                s = 0
                for i in range(lv):
                    s+= 1.025**i
                self.point2A = s
            self.pointplayer1=self.point0A + self.point1A + self.point2A
        self.BB.player1.lv_point = self.BB.player1.maxlv_point - self.pointplayer1
        if player == 1:
            if id == 0:
                s = 0
                for i in range(lv):
                    s+= 1.025**i
                self.point0B = s
            if id == 1:
                s=0
                for i in range(lv):
                    s+= 1.025**i
                self.point1B = s
            if id == 2:
                s = 0
                for i in range(lv):
                    s+= 1.025**i
                self.point2B = s
            self.pointplayer2=self.point0B + self.point1B + self.point2B
        self.BB.player2.lv_point = self.BB.player2.maxlv_point - self.pointplayer2

    def skill_points(self, player, id, lv):
        self.AA.listplayer[player][id].skill_lv = lv
        


    def connected(self):
        return self.ready
