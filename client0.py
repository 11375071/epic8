import pygame
from network import Network
pygame.font.init()
import os

width = 1280
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

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
   
hit_or_not=False
player=-1
lv = [0,0,0]
roll_ball_x=[width*0.75, width*0.75, width*0.75]
num=[[],[]]
for j in range(3):
    num[0].append([0,0,0,0,0,0,0,0])
    num[1].append([0,0,0,0,0,0,0,0])
skill_level=[]
for j in range(2):
    skill_level.append([0,0,0])

def character_surface(character_id):
    global hit_or_not, player, n,lv,roll_ball_x,num,skill_level
    clock = pygame.time.Clock()
    run = True
    
    roll_ball_y=300 
    
    while run:
        clock.tick(60)
        try:
            game = n.send("get")                             ############
        except:
            run = False
            print("Couldn't get game")
            break
        
        window.fill((8,128,128))
        roll_ball=pygame.image.load(".\image\滑动块.jpg")
        roll_strip=pygame.image.load(".\image\滑动条.jpg")
        window.blit(roll_strip,(width*0.75,305))
        window.blit(roll_ball,(roll_ball_x[character_id],roll_ball_y))
 
        if character_id==0:
            myimage="character1.jpg"
        if character_id==1:
            myimage="character2.jpg"
        if character_id==2:
            myimage="character3.jpg"
        
        Image(myimage,ratio=0.7).draw(window, width * 0.19, height * 0.43)
        button_back.draw(window, width * 0.87, height * 0.87)

        reset_image=ButtonImage("重置.jpg",ratio=1)
        reset_image.draw(window, width * 0.82 , height * 0.54)
        
        
        image1=ButtonImage("加号.jpg",ratio=0.5)
        image2=ButtonImage("加号.jpg",ratio=0.5)
        image3=ButtonImage("加号.jpg",ratio=0.5)
        image4=ButtonImage("加号.jpg",ratio=0.5)
        image5=ButtonImage("加号.jpg",ratio=0.5)
        image6=ButtonImage("加号.jpg",ratio=0.5)
        image7=ButtonImage("加号.jpg",ratio=0.5)
        image8=ButtonImage("加号.jpg",ratio=0.5)
        smallbutton=[image1,image2,image3,image4,image5,image6,image7,image8]        
        for i in range(8):
            smallbutton[i].draw(window, width * 0.59, height * (0.141 + 0.05 * i))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_back.handle_event(index)
                
                reset_image.handle_event(statistics_reset,[player,character_id,lv[character_id]])
                if reset_image.handle_event(statistics_reset,[player,character_id,lv[character_id]]):
                    roll_ball_x[character_id] = width*0.75
                    num=[[],[]]
                    for j in range(3):
                        num[0].append([0,0,0,0,0,0,0,0])
                        num[1].append([0,0,0,0,0,0,0,0])
                
                for i in range(8):
                    smallbutton[i].handle_event(extra_up,[player,character_id,lv[character_id],i])
                    if smallbutton[i].handle_event(extra_up,[player,character_id,lv[character_id],i]):
                        if lv[character_id] == 80:
                            num[player][character_id][i]+=1
                x, y = event.pos
                if roll_ball_x[character_id]<=x<=roll_ball_x[character_id]+20 and roll_ball_y<=y<=roll_ball_y+40:
                    hit_or_not=True
            if event.type == pygame.MOUSEBUTTONUP and hit_or_not==True:
                hit_or_not=False
            
            if hit_or_not==True and roll_ball_x[character_id] < width*0.75+280:
                if event.type == pygame.MOUSEMOTION:
                    xx,yy=event.pos
                    roll_ball_x[character_id]=xx-10
                    if roll_ball_x[character_id]<width*0.75:
                        roll_ball_x[character_id]=width*0.75
                    if roll_ball_x[character_id]>width*0.75+280:
                        roll_ball_x[character_id]=width*0.75+280
                        hit_or_not=False      
            lv[character_id]=int((roll_ball_x[character_id]-width*0.75)/280*80)
        s=0
        for i in range(8) :
            s +=num[player][character_id][i]
        skill_level[player][character_id]=s    
        
        n.send(str(player)+"I"+str(character_id)+"I"+str(skill_level[player][character_id])+"I"+"65536")

        for i in range(8) :
            if num[player][character_id][i] != 0:
                Text("+"+str(num[player][character_id][i]),Color.RED,"msyh.ttc",20).draw(window,width*0.545,height*(0.12+0.05*i))



        Text("攻击",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.12)
        Text("防御",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.17)
        Text("生命值",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.22)
        Text("暴击",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.27)
        Text("暴伤",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.32)
        Text("效果命中",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.37)
        Text("效果抵抗",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.42)
        Text("速度",Color.WHITE,"msyh.ttc",20).draw(window,width*0.38,height*0.47)

        
        n.send(str(player) + "I" + str(character_id) + "I" + str(lv[character_id]) + "I" + "95559")
        
        Text("player"+str(player+1),Color.WHITE,"msyh.ttc",50).draw(window,width*0.75,height*0.03)
        if player == 0:
            if game.BB.player1.lv_point >= 0:
                Text("剩余经验点:"+str(int(game.BB.player1.lv_point)),Color.WHITE,"msyh.ttc",30).draw(window,width*0.77,height*0.14)
            if game.BB.player1.lv_point < 0:
                Text("剩余经验点:"+str(int(game.BB.player1.lv_point)),Color.RED,"msyh.ttc",30).draw(window,width*0.77,height*0.14)
        if player == 1:
            if game.BB.player2.lv_point >= 0:
                Text("剩余经验点:"+str(int(game.BB.player2.lv_point)),Color.WHITE,"msyh.ttc",30).draw(window,width*0.77,height*0.14)
            if game.BB.player2.lv_point < 0:
                Text("剩余经验点:"+str(int(game.BB.player2.lv_point)),Color.RED,"msyh.ttc",30).draw(window,width*0.77,height*0.14)
            
        Text("等级 "+str(game.AA.listplayer[player][character_id].lv)+"/80",Color.WHITE,"msyh.ttc",50).draw(window,width*0.48,height*0.01)
        Text("+"+str(game.AA.listplayer[player][character_id].skill_lv),Color.RED,"msyh.ttc",50).draw(window,width*0.66,height*0.01)
        Text(str(int(game.AA.listplayer[player][character_id].atk)),Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.12)
        Text(str(int(game.AA.listplayer[player][character_id].df)),Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.17)
        Text(str(int(game.AA.listplayer[player][character_id].hp)),Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.22)
        Text(str(round(game.AA.listplayer[player][character_id].crit*100,1))+"%",Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.27)
        Text(str(int(game.AA.listplayer[player][character_id].crit_damage*100))+"%",Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.32)
        Text(str(round(game.AA.listplayer[player][character_id].effect_hit*100,1))+"%",Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.37)
        Text(str(round(game.AA.listplayer[player][character_id].effect_defend*100,1))+"%",Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.42)
        Text(str(int(game.AA.listplayer[player][character_id].speed)),Color.WHITE,"msyh.ttc",20).draw(window,width*0.47,height*0.47)
               
        pygame.display.update()

def extra_up(list):
    n.send(str(list[0])+"I" + str(list[1]) + "I"+ str(list[2]) +"I"+ str(list[3])+"I"+"75884")

def statistics_reset(list):
    n.send(str(list[0])+"I" + str(list[1]) + "I"+ str(list[2]) +"I"+ "36912")
   
    
    

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
        center_x, center_y: 文本放置在表面的<中心坐标>
        """

        surface.blit(self.text_image, (center_x, center_y))

class Image:
    def __init__(self, img_name: str, ratio=1):
        """
        img_name: 图片文件名，如'enteground.jpg'、'ink.png',注意为字符串
        ratio: 图片缩放比例，与主屏幕相适应，默认值为0.4
        """
        self.img_name = img_name
        self.ratio = ratio

        self.original_img = pygame.image.load(os.path.join('image', self.img_name))
        self.img_width = self.original_img.get_width()
        self.img_height = self.original_img.get_height()

        self.size_scaled = self.img_width * self.ratio, self.img_height * self.ratio             #######################################

        self.image_scaled = pygame.transform.smoothscale(self.original_img, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 图片放置的表面
        center_x, center_y: 图片放置在表面的<中心坐标>
        """
        upperleft_x = center_x - self.img_width_scaled / 2
        upperleft_y = center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (upperleft_x, upperleft_y))

class ButtonImage(Image):
    def __init__(self, img_name: str, ratio=0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y                       ############################################

    def handle_event(self, command, *args):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command(*args)
            return True

button_level_up=ButtonImage("up.jpg")
button_back = ButtonImage("返回.jpg")
button_enter_1 = ButtonImage("character1.jpg")
button_enter_2 = ButtonImage("character2.jpg")
button_enter_3 = ButtonImage("character3.jpg")

def redrawWindow(window, game):
    window.fill((128,128,128))
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:    
        button_enter_1.draw(window, width * 0.14, height * 0.27)
        button_enter_2.draw(window, width * 0.34, height * 0.27)
        button_enter_3.draw(window, width * 0.54, height * 0.27)

    pygame.display.update()

imageone=ButtonImage("character1.jpg")

def get_network():
    global player,n
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    
def index():
    global player,n
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        try:
            game = n.send("get")                             ############
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

        redrawWindow(window, game)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        window.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        window.blit(text, (100,200))
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