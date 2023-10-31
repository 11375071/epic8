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
        self.character1A = character(0, 0, 1200, 1200, 1400, 1400, 25000, 25000, 220, 220, 0.15, 0.15, 1.1, 1.1, 0.9, 0.9, 1.2, 1.2)
        self.character1B = character(0, 0, 1200, 1200, 1400, 1400, 25000, 25000, 220, 220, 0.15, 0.15, 1.1, 1.1, 0.9, 0.9, 1.2, 1.2)
        self.character2A = character(0, 0, 2400, 2400, 900, 900, 9500, 9500, 300, 300, 0.35, 0.35, 1.4, 1.4, 1.6, 1.6, 0.2, 0.2)
        self.character2B = character(0, 0, 2400, 2400, 900, 900, 9500, 9500, 300, 300, 0.35, 0.35, 1.4, 1.4, 1.6, 1.6, 0.2, 0.2)
        self.character3A = character(0, 0, 3500, 3500, 1100, 1100, 12000, 10000, 225, 225, 0.48, 0.48, 1.8, 1.8, 0.1, 0.1, 0.2, 0.2)
        self.character3B = character(0, 0, 3500, 3500, 1100, 1100, 12000, 10000, 225, 225, 0.48, 0.48, 1.8, 1.8, 0.1, 0.1, 0.2, 0.2)

        self.list_playerone = [self.character1A, self.character2A, self.character3A]
        self.list_playertwo = [self.character1B, self.character2B, self.character3B]

        self.listplayer = [self.list_playerone, self.list_playertwo]

class player_data:
    def __init__(self, lv_point, maxlv_point, skill_point, maxskill_point):
        self.lv_point = lv_point
        self.skill_point = skill_point
        self.maxlv_point = maxlv_point
        self.maxskill_point = maxskill_point

class players:
    def __init__(self):
        self.player1 = player_data(1000, 1000, 50, 50)
        self.player2 = player_data(1000, 1000, 50, 50)
