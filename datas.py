class character:
    def __init__(self, maxatk, maxdf, maxhp, maxspeed, maxcrit, maxcrit_damage, maxeffect_hit, maxeffect_defend):
        self.lv = 0
        self.skill_lv = 0
        self.atk = 0
        self.maxatk = maxatk
        self.df = 0
        self.maxdf = maxdf
        self.hp = 0
        self.maxhp = maxhp
        self.speed = maxspeed
        self.maxspeed = maxspeed
        self.crit = 0
        self.maxcrit = maxcrit
        self.crit_damage = 0
        self.maxcrit_damage = maxcrit_damage
        self.effect_hit = maxeffect_hit
        self.maxeffect_hit = maxeffect_hit
        self.effect_defend = maxeffect_defend
        self.maxeffect_defend = maxeffect_defend

class characters:
    def __init__(self):
        self.character1A = character(maxatk=5800, maxdf=-300, maxhp=18000, maxspeed=270, maxcrit=0.36, maxcrit_damage=1.5, maxeffect_hit=9999.99, maxeffect_defend=9999.99)
        self.character1B = character(maxatk=5800, maxdf=-300, maxhp=18000, maxspeed=270, maxcrit=0.36, maxcrit_damage=1.5, maxeffect_hit=9999.99, maxeffect_defend=9999.99)
        self.character2A = character(maxatk=3600, maxdf=1200, maxhp=9500, maxspeed=9999, maxcrit=9999.99, maxcrit_damage=1.7, maxeffect_hit=9999.99, maxeffect_defend=9999.99)
        self.character2B = character(maxatk=3600, maxdf=1200, maxhp=9500, maxspeed=9999, maxcrit=9999.99, maxcrit_damage=1.7, maxeffect_hit=9999.99, maxeffect_defend=9999.99)
        self.character3A = character(maxatk=1800, maxdf=4300, maxhp=39000, maxspeed=225, maxcrit=0.24, maxcrit_damage=3.6, maxeffect_hit=0, maxeffect_defend=0)
        self.character3B = character(maxatk=1800, maxdf=4300, maxhp=39000, maxspeed=225, maxcrit=0.24, maxcrit_damage=3.6, maxeffect_hit=0, maxeffect_defend=0)
        self.character4A = character(maxatk=12999, maxdf=1600, maxhp=21500, maxspeed=200, maxcrit=0.22, maxcrit_damage=-0.60, maxeffect_hit=0, maxeffect_defend=0)
        self.character4B = character(maxatk=12999, maxdf=1600, maxhp=21500, maxspeed=200, maxcrit=0.22, maxcrit_damage=-0.60, maxeffect_hit=0, maxeffect_defend=0)
        self.character5A = character(maxatk=7200, maxdf=1500, maxhp=22222, maxspeed=-9999, maxcrit=-80, maxcrit_damage=-99, maxeffect_hit=-9999.99, maxeffect_defend=-9999.99)
        self.character5B = character(maxatk=7200, maxdf=1500, maxhp=22222, maxspeed=-9999, maxcrit=-80, maxcrit_damage=-99, maxeffect_hit=-9999.99, maxeffect_defend=-9999.99)

        self.list_playerone = [self.character1A, self.character2A, self.character3A, self.character4A, self.character5A]
        self.list_playertwo = [self.character1B, self.character2B, self.character3B, self.character4B, self.character5B]

        self.listplayer = [self.list_playerone, self.list_playertwo]

class player_data:
    def __init__(self, lv_point, maxlv_point, skill_point, maxskill_point):
        self.lv_point = lv_point
        self.skill_point = skill_point
        self.maxlv_point = maxlv_point
        self.maxskill_point = maxskill_point

class players:
    def __init__(self):
        self.players = [player_data(9999, 9999, 30, 30), player_data(9999, 9999, 30, 30)]

class atk_skill:
    def __init__(self,atk_rate,breakthrough_rate,hit_rate):
        self.atk_rate=atk_rate
        self.breakthrough_rate=breakthrough_rate
        self.hit_rate=hit_rate

class skills:
    def __init__(self):
        self.skill = atk_skill(1, 0, 1)


