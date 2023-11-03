class character:
    def __init__(self, lv, skill_lv, maxatk, atk, df, maxdf, hp, maxhp, speed, maxspeed, crit, maxcrit, crit_damage, maxcrit_damage, effect_hit, maxeffect_hit, effect_defend, maxeffect_defend):
        self.lv = lv
        self.skill_lv=skill_lv
        self.atk = atk
        self.maxatk = maxatk
        self.df = df
        self.maxdf = maxdf
        self.hp = hp
        self.maxhp = maxhp
        self.speed = speed
        self.maxspeed = maxspeed
        self.crit = crit
        self.maxcrit = maxcrit
        self.crit_damage = crit_damage
        self.maxcrit_damage = maxcrit_damage
        self.effect_hit = effect_hit
        self.maxeffect_hit = maxeffect_hit
        self.effect_defend = effect_defend
        self.maxeffect_defend = maxeffect_defend

class characters:
    def __init__(self):
        self.character1A = character(0, 0, 6200, 6200, 400, 400, 15000, 15000, 220, 220, 0.55, 0.55, 1.6, 1.6, 9999.99, 9999.99, 9999.99, 9999.99)
        self.character1B = character(0, 0, 6200, 6200, 400, 400, 15000, 15000, 220, 220, 0.55, 0.55, 1.6, 1.6, 9999.99, 9999.99, 9999.99, 9999.99)
        self.character2A = character(0, 0, 2400, 2400, 900, 900, 24500, 24500, 9999, 9999, 9999.99, 9999.99, 1.4, 1.4, 9999.99, 9999.99, 9999.99, 9999.99)
        self.character2B = character(0, 0, 2400, 2400, 900, 900, 24500, 24500, 9999, 9999, 9999.99, 9999.99, 1.4, 1.4, 9999.99, 9999.99, 9999.99, 9999.99)
        self.character3A = character(0, 0, 1900, 1900, 2900, 2900, 7000, 7000, 225, 225, 0.2, 0.2, 1.8, 1.8, 0, 0, 0, 0)
        self.character3B = character(0, 0, 1900, 1900, 2900, 2900, 7000, 7000, 225, 225, 0.2, 0.2, 1.8, 1.8, 0, 0, 0, 0)
        self.character4A = character(0, 0, 3700, 3700, 1600, 1600, 28500, 28500, 200, 200, 0.42, 0.42, 1.65, 1.65, 0, 0, 0, 0)
        self.character4B = character(0, 0, 3700, 3700, 1600, 1600, 28500, 28500, 200, 200, 0.42, 0.42, 1.65, 1.65, 0, 0, 0, 0)
        self.character5A = character(0, 0, 7600, 7600, 1500, 1500, 17500, 17500, -9999, -9999, -80, -80, -99, -99, -9999.99, -9999.99, -9999.99, -9999.99)
        self.character5B = character(0, 0, 7600, 7600, 1500, 1500, 17500, 17500, -9999, -9999, -80, -80, -99, -99, -9999.99, -9999.99, -9999.99, -9999.99)

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
        self.players = [player_data(9999, 9999, 35, 35), player_data(9999, 9999, 35, 35)]

class atk_skill:
    def __init__(self,atk_rate,breakthrough_rate,hit_rate):
        self.atk_rate=atk_rate
        self.breakthrough_rate=breakthrough_rate
        self.hit_rate=hit_rate

class skills:
    def __init__(self):
        self.skill = atk_skill(1, 0, 1)


