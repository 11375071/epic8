import datas
import numpy as np

class Game:
    def __init__(self,id):
        self.ready = False
        self.id = id
        
        self.num0 = -1
        self.num1 = -1
        self.pt0 = 40
        self.pt1 = 40
        self.AA = datas.characters()
        self.BB = datas.players()
        self.points = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.skill_points = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.pointplayers = [0, 0]
        self.person_id = 0
        self.start_play = [False, False]
        self.data_list=[]
        self.new_data_list=[]
        self.original_data_list=[]
        self.speed=[]
        self.characterid_record = [[], []]
        self.turn = [0, 0]
        self.log = ""

    def up_lv(self, player, id, lv):
        if self.AA.listplayer[player][id].lv!=80:
            self.AA.listplayer[player][id].hp = lv*self.AA.listplayer[player][id].maxhp*0.015+self.AA.listplayer[player][id].maxhp
            self.AA.listplayer[player][id].atk = lv*self.AA.listplayer[player][id].maxatk*0.012+self.AA.listplayer[player][id].maxatk
            self.AA.listplayer[player][id].df = lv*self.AA.listplayer[player][id].maxdf*0.012+self.AA.listplayer[player][id].maxdf
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
                self.AA.listplayer[player][id].crit += (0.03 + self.AA.listplayer[player][id].maxcrit*0.08)
            if num == 4:
                self.AA.listplayer[player][id].crit_damage += (0.07 + self.AA.listplayer[player][id].maxcrit_damage / 15)
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
        self.AA.listplayer[player][id].speed = self.AA.listplayer[player][id].maxspeed
        self.AA.listplayer[player][id].skill_lv = 0
        self.AA.listplayer[player][id].lv = 0
        

    def point_consume(self, player, id, lv):
        s = 0
        for i in range(lv):
            s+= 1.025**i
        self.points[player][id] = s
        self.pointplayers[player]=sum(self.points[player])
        self.BB.players[player].lv_point = self.BB.players[player].maxlv_point - self.pointplayers[player]

    def up_skill_lv(self, player, id, lv):
        self.AA.listplayer[player][id].skill_lv = lv
        self.skill_points[player][id] = lv
        self.BB.players[player].skill_point = self.BB.players[player].maxskill_point - sum(self.skill_points[player])
    
    def people_judge(self, player, c0, c1):
        assert(self.BB.players[player].lv_point >= 0)
        assert(self.BB.players[player].skill_point >= 0)
        self.start_play[player] = True
        self.characterid_record[player] = [c0, c1]
        self.order_judge(player, c0)
        self.order_judge(player, c1)

    def trigger(self):
        return (self.start_play[0] and self.start_play[1])
    
    def order_judge(self, player, id):
        if [player,id] not in self.data_list:
            self.data_list.append([player,id])
            self.original_data_list.append([player,id])
        if len(self.data_list)==4:
            # t=0
            # max=[0,0,0,0,0,0,0]
            # i_record=[-1,-1,-1,-1,-1,-1,-1]
            # for i in range(len(self.data_list)):
            #     self.speed.append(self.AA.listplayer[self.data_list[i][0]][self.data_list[i][1]].speed)   #记录所有速度数值
            # while t<4:
            #     for i in range(len(self.data_list)):     #查找最大
            #         if max[t] < self.speed[i] and self.speed[i] not in max:
            #             max[t] = self.speed[i]
            #             i_record[t] = i
            #     self.new_data_list.append(self.data_list[i_record[t]])
            #     t += 1
            #     for r in range(4):
            #         for i in range(len(self.data_list)-1,-1,-1):
            #             if self.speed[i] == max[t-1] and i not in i_record:
            #                 i_record[t]=i
            #                 self.new_data_list.append(self.data_list[i_record[t]])
            #                 t += 1
            self.data_list.sort(key=lambda x:self.AA.listplayer[x[0]][x[1]].speed, reverse=True)

        # (还可以不是4)
    def data_return(self) -> list:    
        if len(self.data_list) == 4:
            return self.data_list
        else:
            return []
            
    def turn_move(self, num, skip=False):
        if skip:
            pass
        else:
            player, id = self.data_list[self.turn[1]]
            opp = 1 - player
            atk_goal = num
            
            hit = self.AA.listplayer[player][id].atk - self.AA.listplayer[opp][self.characterid_record[opp][atk_goal]].df
            if np.random.rand() < self.AA.listplayer[player][id].crit:
                hit *= self.AA.listplayer[player][id].crit_damage
                
            self.AA.listplayer[opp][self.characterid_record[opp][atk_goal]].hp -= hit
            self.log = "player" + str(player) + "对player" + str(opp) + "造成了" + str(hit) + "点伤害"
        self.turn[1] += 1
        if self.turn[1] == len(self.characterid_record[0] * 2):
            self.order_judge(0, self.characterid_record[0][0])
            self.turn[0] += 1
            self.turn[1] = 0
        
        player, id = self.data_list[self.turn[1]]
        if self.AA.listplayer[player][id].hp <= 0:
            self.turn_move(num, skip=True)
            
        print(self.turn, self.data_list[self.turn[1]])
            
    def get_turn(self):
        return self.turn
             
    def connected(self):
        return self.ready

# a=Game(5)
# aa=a.order_judge(0,1)
# b=a.order_judge(0,2)
# c=a.order_judge(1,4)
# d=a.order_judge(1,2)

        
