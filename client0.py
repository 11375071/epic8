import pygame
import math
from network import Network
pygame.font.init()
import os

width = 1280
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Epic8")

class Color:
    # 自定义颜色
    ACHIEVEMENT = (220, 160, 87)
    VERSION = (220, 160, 87)

    # 固定颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)  # 中性灰
    TRANSPARENT = (255, 255, 255, 0)  # 白色的完全透明
   
hit_or_not = False
player = -1
lv = [0, 0, 0, 0, 0]
roll_ball_x = [width * 0.75, width * 0.75, width * 0.75, width * 0.75, width * 0.75]
num = []
for i in range(5):
    num.append([0]*8)
skill_level = []
for j in range(2):
    skill_level.append([0, 0, 0, 0, 0])

def f(x):
    if x <= 0:
        return 0
    else:
        return max(0, math.log(x / 800) + 0.00007*x) * 10

def character_surface(character_id):
    global hit_or_not, player, n, lv, roll_ball_x, num, skill_level
    clock = pygame.time.Clock()
    run = True
    
    roll_ball_y = 300 
    
    while run:
        clock.tick(60)
        try:
            game = n.send("get")                             
        except:
            run = False
            print("Couldn't get game")
            break
        
        window.fill((8, 128, 128))
        roll_ball = pygame.image.load(".\image\滑动块.jpg")
        roll_strip = pygame.image.load(".\image\滑动条.jpg")
        window.blit(roll_strip, (width * 0.75, 305))
        window.blit(roll_ball, (roll_ball_x[character_id], roll_ball_y))
 
        if character_id == 0:
            myimage = "character1.jpg"
        if character_id == 1:
            myimage = "character2.jpg"
        if character_id == 2:
            myimage = "character3.jpg"
        if character_id == 3:
            myimage = "character4.jpg"
        if character_id == 4:
            myimage = "character5.jpg"
        
        Image(myimage, ratio = 0.7).draw(window, width * 0.19, height * 0.43)
        button_back.draw(window, width * 0.87, height * 0.87)

        reset_image = ButtonImage("重置.jpg", ratio = 1)
        reset_image.draw(window, width * 0.82 , height * 0.54)
        
        image1 = ButtonImage("加号.jpg", ratio = 0.5)
        image2 = ButtonImage("加号.jpg", ratio = 0.5)
        image3 = ButtonImage("加号.jpg", ratio = 0.5)
        image4 = ButtonImage("加号.jpg", ratio = 0.5)
        image5 = ButtonImage("加号.jpg", ratio = 0.5)
        image6 = ButtonImage("加号.jpg", ratio = 0.5)
        image7 = ButtonImage("加号.jpg", ratio = 0.5)
        image8 = ButtonImage("加号.jpg", ratio = 0.5)
        smallbutton = [image1, image2, image3, image4, image5, image6, image7, image8]        
        for i in range(8):
            smallbutton[i].draw(window, width * 0.59, height * (0.141 + 0.05 * i))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_back.handle_event(index)
                if reset_image.handle_event(statistics_reset, [player, character_id, lv[character_id]]):
                    roll_ball_x[character_id] = width * 0.75
                    num[character_id] = [0]*8
                
                for i in range(8):
                    if smallbutton[i].handle_event(extra_up, [player, character_id, lv[character_id], i]):
                        if lv[character_id] == 80:
                            num[character_id][i] += 1
                x, y = event.pos
                if roll_ball_x[character_id] <= x <= roll_ball_x[character_id] + 20 and roll_ball_y <= y <= roll_ball_y + 40:
                    hit_or_not = True
            if event.type == pygame.MOUSEBUTTONUP and hit_or_not == True:
                hit_or_not = False
            
            if hit_or_not == True and roll_ball_x[character_id] < width * 0.75 + 280:
                if event.type == pygame.MOUSEMOTION:
                    xx, yy = event.pos
                    roll_ball_x[character_id] = xx-10
                    if roll_ball_x[character_id] < width * 0.75:
                        roll_ball_x[character_id] = width * 0.75
                    if roll_ball_x[character_id] > width * 0.75 + 280:
                        roll_ball_x[character_id] = width * 0.75 + 280
                        hit_or_not = False      
            lv[character_id] = int((roll_ball_x[character_id]-width * 0.75) / 280 * 80)
        s = 0
        for i in range(8) :
            s += num[character_id][i]
        skill_level[player][character_id] = s
        
        n.send(str(player) + "I" + str(character_id) + "I" + str(skill_level[player][character_id]) + "I" + "65536")

        for i in range(8) :
            if num[character_id][i] != 0:
                Text(" + " + str(num[character_id][i]), Color.RED, "msyh.ttc", 20).draw(window, width * 0.545, height * (0.12 + 0.05 * i))

        Text("攻击", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.12)
        Text("防御", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.17)
        Text("生命值", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.22)
        Text("暴击", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.27)
        Text("暴伤", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.32)
        Text("效果命中", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.37)
        Text("效果抵抗", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.42)
        Text("速度", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.38, height * 0.47)

        
        n.send(str(player) + "I" + str(character_id) + "I" + str(lv[character_id]) + "I" + "clvup")
        Text("player" + str(player + 1), Color.WHITE, "msyh.ttc", 50).draw(window, width * 0.75, height * 0.03)

        if game.BB.players[player].lv_point >= 0:
            Text("剩余经验点:" + str(int(game.BB.players[player].lv_point)), Color.WHITE, "msyh.ttc", 30).draw(window, width * 0.77, height * 0.14)
        if game.BB.players[player].lv_point < 0:
            Text("剩余经验点:" + str(int(game.BB.players[player].lv_point)), Color.RED, "msyh.ttc", 30).draw(window, width * 0.77, height * 0.14)
          
        if game.BB.players[player].skill_point >= 0:
            Text("剩余技能点:" + str(int(game.BB.players[player].skill_point)), Color.WHITE, "msyh.ttc", 30).draw(window, width * 0.77, height * 0.19)
        if game.BB.players[player].skill_point < 0:
            Text("剩余技能点:" + str(int(game.BB.players[player].skill_point)), Color.RED, "msyh.ttc", 30).draw(window, width * 0.77, height * 0.19)
          
          
        Text("等级 " + str(game.AA.listplayer[player][character_id].lv) + " / 80", Color.WHITE, "msyh.ttc", 50).draw(window, width * 0.48, height * 0.01)
        Text(" + " + str(game.AA.listplayer[player][character_id].skill_lv), Color.RED, "msyh.ttc", 50).draw(window, width * 0.68, height * 0.01)
        Text(str(int(game.AA.listplayer[player][character_id].atk)), Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.12)
        Text(str(int(game.AA.listplayer[player][character_id].df)), Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.17)
        Text(str(int(game.AA.listplayer[player][character_id].hp)), Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.22)
        Text(str(round(game.AA.listplayer[player][character_id].crit * 100, 1)) + "%", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.27)
        Text(str(int(game.AA.listplayer[player][character_id].crit_damage * 100)) + "%", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.32)
        Text(str(round(game.AA.listplayer[player][character_id].effect_hit * 100, 1)) + "%", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.37)
        Text(str(round(game.AA.listplayer[player][character_id].effect_defend * 100, 1)) + "%", Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.42)
        Text(str(int(game.AA.listplayer[player][character_id].speed)), Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.47, height * 0.47)
               
        pygame.display.update()

def extra_up(list):
    n.send(str(list[0]) + "I" + str(list[1]) + "I" +  str(list[2])  + "I" +  str(list[3]) + "I" + "elvup")

def statistics_reset(list):
    n.send(str(list[0]) + "I" + str(list[1]) + "I" +  str(list[2])  + "I" +  "reset")

class Text:
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):

        self.text = text
        self.text_color = text_color
        self.font_type = font_type
        self.font_size = font_size

        font = pygame.font.Font(os.path.join('font', (self.font_type)), self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()

        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 文本放置的表面
        center_x, center_y: 文本放置在表面的 < 中心坐标 > 
        """

        surface.blit(self.text_image, (center_x, center_y))

class Image:
    def __init__(self, img_name: str, ratio = 1):
        """
        img_name: 图片文件名，如'enteground.jpg'、'ink.png', 注意为字符串
        ratio: 图片缩放比例，与主屏幕相适应，默认值为0.4
        """
        self.img_name = img_name
        self.ratio = ratio

        self.original_img = pygame.image.load(os.path.join('image', self.img_name))
        self.img_width = self.original_img.get_width()
        self.img_height = self.original_img.get_height()

        self.size_scaled = self.img_width * self.ratio, self.img_height * self.ratio             ###

        self.image_scaled = pygame.transform.smoothscale(self.original_img, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 图片放置的表面
        center_x, center_y: 图片放置在表面的 < 中心坐标 > 
        """
        upperleft_x = center_x - self.img_width_scaled / 2
        upperleft_y = center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (upperleft_x, upperleft_y))

class ButtonImage(Image):
    def __init__(self, img_name: str, ratio = 0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y                       

    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)
            return True


button_back = ButtonImage("返回.jpg")
button_enter_1 = ButtonImage("character1.jpg", ratio = 0.35)
button_enter_2 = ButtonImage("character2.jpg", ratio = 0.35)
button_enter_3 = ButtonImage("character3.jpg", ratio = 0.35)
button_enter_4 = ButtonImage("character4.jpg", ratio = 0.35)
button_enter_5 = ButtonImage("character5.jpg", ratio = 0.35)
start_game_button = ButtonImage("开始游戏.jpg", ratio = 0.6)

def redrawWindow(window, game):
    window.fill((128, 128, 128))
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
        window.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    else:    
        button_enter_1.draw(window, width * 0.14, height * 0.27)
        button_enter_2.draw(window, width * 0.34, height * 0.27)
        button_enter_3.draw(window, width * 0.54, height * 0.27)
        button_enter_4.draw(window, width * 0.14, height * 0.74)
        button_enter_5.draw(window, width * 0.34, height * 0.74)
        start_game_button.draw(window, width * 0.85, height * 0.92)

    pygame.display.update()

def get_network():
    global player, n
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    
def index():
    global player, n
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        try:
            game = n.send("get")                             
        except:
            run = False
            print("Couldn't get game")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                button_enter_1.handle_event(character_surface, 0)
                button_enter_2.handle_event(character_surface, 1)
                button_enter_3.handle_event(character_surface, 2) 
                button_enter_4.handle_event(character_surface, 3)
                button_enter_5.handle_event(character_surface, 4)
                start_game_button.handle_event(choose_page)       

        redrawWindow(window, game)

pos_x = width * 0.4
pos_y = height * 0.83
def choose_page():
    global player, something
    something = [False, False, False, False, False]
    characterid_record = []
    clock = pygame.time.Clock()
    run = True

    image1 = ButtonImage("character1.jpg", ratio = 0.12)
    image2 = ButtonImage("character2.jpg", ratio = 0.12)
    image3 = ButtonImage("character3.jpg", ratio = 0.12)
    image4 = ButtonImage("character4.jpg", ratio = 0.12)
    image5 = ButtonImage("character5.jpg", ratio = 0.12)

    image_cancel = ButtonImage("取消.jpg", ratio = 0.6)
    image_confirm = ButtonImage("确定.JPG", ratio = 0.6)
    image = ["character1.jpg", "character2.jpg", "character3.jpg", "character4.jpg", "character5.jpg"]
    while run:
        clock.tick(60)
        window.fill((8, 128, 128))

        for i in range(2) :
            Image("未知.png", ratio = 0.52).draw(window, width * (0.33 + 0.33 * i), height * 0.4)
        
        image1.draw(window, pos_x, pos_y)
        image2.draw(window, pos_x + 100, pos_y)
        image3.draw(window, pos_x + 200, pos_y)
        image4.draw(window, pos_x + 300, pos_y)
        image5.draw(window, pos_x + 400, pos_y)
        image_cancel.draw(window, width * 0.9, height * 0.93)
        image_confirm.draw(window, width * 0.8, height * 0.93)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                image_cancel.handle_event(index)
                image1.handle_event(empty, 0)
                image2.handle_event(empty, 1)
                image3.handle_event(empty, 2)
                image4.handle_event(empty, 3)
                image5.handle_event(empty, 4)
                if len(characterid_record) == 2 :
                    image_confirm.handle_event(battle_start, characterid_record)
        for i in range(5):
            if something[i] == True:
                if i not in characterid_record:
                    characterid_record.append(i)
            if something[i] == False:
                if i in characterid_record:
                    characterid_record.remove(i)
        if 1  <= len(characterid_record)  <= 2: 
            for i in range(len(characterid_record)):
                Image(image[characterid_record[i]], ratio = 0.5).draw(window, width * (0.33 + 0.33 * i), height * 0.4)
                Image("准备中.png", ratio = 0.5).draw(window, width * (0.33 + 0.33 * i), height * 0.4)
        if len(characterid_record) > 2: 
            something = [False, False, False, False, False]

        pygame.display.update()

something = [False, False, False, False, False]

def empty(par):
    global something
    something[par] = 1 - something[par]

def battle_start(characterid_record):
    global n, player
    n.send(str(player) + "I" + str(characterid_record[0]) + "I" + str(characterid_record[1]) + "I" + "btstt")
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        window.fill((128, 128, 128))

        try:
            game = n.send("get")                             
        except:
            run = False
            print("Couldn't get game")
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
              
        if game.trigger() == False:
            font = pygame.font.SysFont("comicsans", 80)
            text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
            window.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
        else:
            really_start()
        
        pygame.display.update()

def move_turn(n, player):
    n.send(str(player) + "I" + "moove")
#############################################
def really_start():
    global n, player
    image1 = ButtonImage("character1.jpg", ratio = 0.2)
    image2 = ButtonImage("character2.jpg", ratio = 0.2)
    image3 = ButtonImage("character3.jpg", ratio = 0.2) 
    image4 = ButtonImage("character4.jpg", ratio = 0.2)
    image5 = ButtonImage("character5.jpg", ratio = 0.2) 
    image_list = [image1, image2, image3, image4, image5]
    blankimage1 = ButtonImage("未知角色.jpg", ratio = 0.2)
    blankimage2 = ButtonImage("未知角色.jpg", ratio = 0.2)
    att = ButtonImage("确定.jpg", ratio = 0.37)

    speed_1 = Image("1.jpg", ratio = 1)
    speed_2 = Image("2.jpg", ratio = 1)
    speed_3 = Image("3.jpg", ratio = 1)
    speed_4 = Image("4.jpg", ratio = 1)
    speed_num_imglist = [speed_1, speed_2, speed_3, speed_4]
    
    image_background = Image("背景.jpg", ratio = 0.8)
    run = True
    clock = pygame.time.Clock()
    # turn  = [ 大回合，小回合]
    jishuqi=0
    original_character_info=[[0,0],[0,0]]
    while run:
        clock.tick(60)
        image_background.draw(window, width * 0.5, height * 0.5)
        try:
            game = n.send("get")                             
        except:
            run = False
            print("Couldn't get game")
        if jishuqi==0:
            jishuqi=1
            for i in range(2):
                original_character_info[player][i]=[game.AA.listplayer[player][game.characterid_record[player][i]].atk,
                                                    game.AA.listplayer[player][game.characterid_record[player][i]].df,
                                                    game.AA.listplayer[player][game.characterid_record[player][i]].hp,
                                                    game.AA.listplayer[player][game.characterid_record[player][i]].speed,
                                                    game.AA.listplayer[player][game.characterid_record[player][i]].crit,
                                                    game.AA.listplayer[player][game.characterid_record[player][i]].crit_damage,
                                                    game.AA.listplayer[player][game.characterid_record[player][i]].effect_hit,
                                                    game.AA.listplayer[player][game.characterid_record[player][i]].effect_defend
                                                    ]
                original_character_info[1-player][i]=[game.AA.listplayer[1-player][game.characterid_record[1-player][i]].atk,
                                                        game.AA.listplayer[1-player][game.characterid_record[1-player][i]].df,
                                                        game.AA.listplayer[1-player][game.characterid_record[1-player][i]].hp,
                                                        game.AA.listplayer[1-player][game.characterid_record[1-player][i]].speed,
                                                        game.AA.listplayer[1-player][game.characterid_record[1-player][i]].crit,
                                                        game.AA.listplayer[1-player][game.characterid_record[1-player][i]].crit_damage,
                                                        game.AA.listplayer[1-player][game.characterid_record[1-player][i]].effect_hit,
                                                        game.AA.listplayer[1-player][game.characterid_record[1-player][i]].effect_defend
                                                        ]
            
        image_list[game.characterid_record[player][0]].draw(window, width * 0.1, height * 0.45)
        image_list[game.characterid_record[player][1]].draw(window, width * 0.2, height * 0.45)
        blankimage1.draw(window, width * 0.8, height * 0.45)
        blankimage2.draw(window, width * 0.9, height * 0.45)
        
        lista = game.data_return()    #返回二维数组，第一层四个元素，每个元素代表敌我的角色id
        turn = game.get_turn()
        Text(game.log, Color.WHITE, "msyh.ttc", 20).draw(window, width * 0.5, height * 0.9)
        if len(lista) != 0:  
            for i in range(len(game.characterid_record[player])):
                if player == 0:
                    speed_num_imglist[lista.index([0, game.characterid_record[0][i]])].draw(window, width * (0.07 + 0.1 * i), height * 0.30)
                    speed_num_imglist[lista.index([1, game.characterid_record[1][i]])].draw(window, width * (0.77 + 0.1 * i), height * 0.30)
                    pygame.draw.rect(window, Color.WHITE, (width * (0.07 + 0.1 * i)-1, height * 0.25-2, 82, 9))
                    pygame.draw.rect(window, Color.WHITE, (width * (0.77 + 0.1 * i)-1, height * 0.25-2, 82, 9))
                    pygame.draw.rect(window, Color.GREEN, (width * (0.07 + 0.1 * i), height * 0.25, game.AA.listplayer[0][game.characterid_record[0][i]].hp/original_character_info[0][i][2]*80, 5))
                    pygame.draw.rect(window, Color.GREEN, (width * (0.77 + 0.1 * i), height * 0.25, game.AA.listplayer[1][game.characterid_record[1][i]].hp/original_character_info[1][i][2]*80, 5))
                
                if player == 1:
                    speed_num_imglist[lista.index([1, game.characterid_record[1][i]])].draw(window, width * (0.07 + 0.1 * i), height * 0.30)
                    speed_num_imglist[lista.index([0, game.characterid_record[0][i]])].draw(window, width * (0.77 + 0.1 * i), height * 0.30)
                    pygame.draw.rect(window, Color.WHITE, (width * (0.07 + 0.1 * i)-1, height * 0.25-2, 82, 9))
                    pygame.draw.rect(window, Color.WHITE, (width * (0.77 + 0.1 * i)-1, height * 0.25-2, 82, 9))
                    pygame.draw.rect(window, Color.GREEN, (width * (0.07 + 0.1 * i), height * 0.25, game.AA.listplayer[1][game.characterid_record[1][i]].hp/original_character_info[1][i][2]*80, 5))
                    pygame.draw.rect(window, Color.GREEN, (width * (0.77 + 0.1 * i), height * 0.25, game.AA.listplayer[0][game.characterid_record[0][i]].hp/original_character_info[0][i][2]*80, 5))
        if lista[turn[1]][0] == player:
            att.draw(window, width * 0.5, height * 0.85)
        
        for i in range(len(game.characterid_record[player])):
            if game.characterid_record[0][i] == lista[turn[1]][1]:
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lista[turn[1]][0] == player:
                    # att.handle_event(move_turn, n, player)
                    blankimage1.handle_event(full, n, player, 0)


                    blankimage2.handle_event(full, n, player, 1)
            
        pygame.display.update()


def full(n, player,num):
    n.send(str(player) + "I" + str(num) + "I" + "90067")
    print(6666666666)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        window.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255, 0, 0))
        window.blit(text, (100, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        

    get_network()
    index()

while True:
    menu_screen()