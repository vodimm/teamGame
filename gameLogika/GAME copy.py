from pygame import *
from random import randint
import time as my_time
import os,sys

white = color.Color("#FFFFFF")
blue = color.Color("#0083ff")
red = color.Color("#fa5127")
width = 242
width2 = 100

app_folder = os.path.dirname(os.path.realpath(sys.argv[0]))

font.init()

#классы
class Player(sprite.Sprite):
    def __init__(self,player_imaged,player_imageu,player_imagel,player_imager, player_x, player_y, size_x, size_y, player_speed, hp):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.imaged = transform.scale(image.load(player_imaged), (size_x, size_y))
        self.imageu = transform.scale(image.load(player_imageu), (size_x, size_y))
        self.imagel = transform.scale(image.load(player_imagel), (size_x, size_y))
        self.imager = transform.scale(image.load(player_imager), (size_x, size_y))
        self.speed_def=player_speed
        self.speed = player_speed+10
        self.list_img=[self.imaged,self.imageu,self.imagel,self.imager]
        self.s=0
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.imaged.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.hp = 100
    def reset(self):
        window.blit(self.list_img[self.s], (self.rect.x, self.rect.y))

    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        global width
        global ch
        global win_x
        global win_y
        global up
        global down
        global right
        global left
        global collide
        keys = key.get_pressed()

        if keys[K_UP] and not self.rect.y <= 0 and left == False and right == False <= 0 or keys[K_w] and not self.rect.y <= 0 and left == False and right == False:
            self.rect.y -= self.speed
            self.s = 1
            up = True
        else:
            up = False

        if keys[K_DOWN] and not self.rect.y >= win_y - 150 and left == False and right == False >= win_y or keys[K_s] and not self.rect.y >= win_y and right == False and left == False:
            self.rect.y += self.speed
            self.s = 0
            down = True
        else:
            down = False

        if keys[K_LEFT] and not self.rect.x <= 0 and down == False and up == False <= 0 or keys[K_a] and not self.rect.x <= 0 and down == False and up == False:
            self.rect.x -= self.speed
            self.s = 2
            left = True
        else:
            left = False

        if keys[K_RIGHT] and not self.rect.x >= win_x and down == False and up == False >= win_x or keys[K_d] and not self.rect.x >= win_x and down == False and up == False:
            self.rect.x += self.speed
            self.s = 3
            right = True
        else:
            right = False

        if keys[K_LSHIFT] and keys[K_LEFT] or keys[K_LSHIFT] and keys[K_s] or keys[K_LSHIFT] and keys[K_d] or keys[K_LSHIFT] and keys[K_w] or keys[K_LSHIFT] and keys[K_a] or keys[K_LSHIFT] and keys[K_RIGHT] or keys[K_LSHIFT] and keys[K_DOWN] or keys[K_LSHIFT] and keys[K_UP]:
            if collide == False:    
                self.speed = self.speed_def + 2
                width -= 2
        elif keys[K_LSHIFT]:
            width+=1
        if width<10:
            self.speed = self.speed_def
        if not keys[K_LSHIFT]:    
            width += 1
            self.speed = self.speed_def
        if width > 242:
            width = 242
        elif width < 1:
            width = 1
    def health(self):
        global wait
        global width2
        global wait_time
        if int(my_time.time() - wait_time) <= 0.5:
            wait = 0
        elif not sprite.collide_rect(monster, self):
            width2 += monster.damage
            self.hp += monster.damage
            wait_time = my_time.time()
        if width2 > 100:
            width2 = 100
    def kill(self):
        global monsters
        global click
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                x,y = mouse.get_pos()
                for room in monsters:
                    for i in range(len(room)):
                        if i - 1 >= 0:
                            if x >= room[i - 1].rect.x - 5 and x <= room[i - 1].rect.x + 35:
                                if y >= room[i - 1].rect.y - 5 and y <= room[i - 1].rect.y + 60:
                                    click += 1
                                    if click == randint(2,4):
                                        del room[i - 1]
                                        click = 0
                                    if click > 4:
                                        click = 0
                        elif i - 1 < 0:
                            if x >= room[i].rect.x and x <= room[i].rect.x + 35:
                                if y >= room[i].rect.y and y <= room[i].rect.y + 60:
                                    click += 1
                                    if click == randint(2,4):
                                        del room[i]
                                        click = 0   
                                    if click > 4:
                                        click = 0                 

class Monster(sprite.Sprite):
    def __init__(self, imaged, imagel, imager, imageu, x, y, size_x, size_y, speed, damage):
        sprite.Sprite.__init__(self)
        self.imaged = transform.scale(image.load(imaged), (size_x, size_y))
        self.imageu = transform.scale(image.load(imageu), (size_x, size_y))
        self.imagel = transform.scale(image.load(imagel), (size_x, size_y))
        self.imager = transform.scale(image.load(imager), (size_x, size_y))

        self.damage = 10
        self.speed = speed
        self.size_x, self.size_y = (size_x, size_y)
        self.rect = self.imaged.get_rect()
        self.rect.x, self.rect.y = (x, y)
        self.list_img=[self.imaged,self.imageu,self.imagel,self.imager]

        self.view = 0
        #cos - costume
    def reset(self):
        window.blit(self.list_img[self.view], (self.rect.x, self.rect.y))

    def AI(self):
        global wait
        global width2
        global wait_time
        if int(my_time.time() - wait_time) <= 0.5:
            wait = 0
        elif sprite.collide_rect(self, hero):
            width2 -= self.damage
            hero.hp -= self.damage
            if hero.hp < 0:
                hero.hp = 0
            elif hero.hp > 100:
                hero.hp = 100
            wait_time = my_time.time()
        if width2 > 100:
            width2 = 100
        elif width2 < 1:
            width2 = 1

        if self.rect.x > hero.rect.x:
            self.rect.x -= self.speed
            self.view = 3
        if hero.rect.x > self.rect.x:
            self.rect.x += self.speed
            self.view = 1
        if hero.rect.x == self.rect.x:
            self.rect.x = hero.rect.x

        if self.rect.y > hero.rect.y:
            self.rect.y -= self.speed
            self.view = 2
        if hero.rect.y > self.rect.y:
            self.rect.y += self.speed
            self.view = 0
        if hero.rect.y == self.rect.y:
            self.rect.y = hero.rect.y   
    def collide(self):
        global monsters
        for room in monsters:
            for i in range(len(room)):
                if len(room) == i + 1:
                    if sprite.collide_rect(room[i], room[i - 1]):
                        if (room[i].rect.x - room[i - 1].rect.x) <= 2:
                            room[i].rect.x -= 1
                            room[i - 1].rect.x += 1
                            if (room[i].rect.y - room[i - 1].rect.y) <= 2:
                                room[i].rect.y -= 1
                                room[i - 1].rect.y += 1     
                elif len(room) == i:
                    if sprite.collide_rect(room[i - 1], room[i - 2]):
                        if (room[i - 1].rect.x - room[i - 2].rect.x) <= 2:
                            room[i - 1].rect.x -= 1
                            room[i - 2].rect.x += 1
                            if (room[i - 1].rect.y - room[i - 2].rect.y) <= 2:
                                room[i - 1].rect.y -= 1
                                room[i - 2].rect.y += 1                         

                
class Wall(sprite.Sprite):
    def __init__(self,width,height,x,y,col1,col2,col3):
        sprite.Sprite.__init__(self)
        self.width=width
        self.height=height
        self.col1=col1
        self.col2=col2
        self.col3=col3
        self.image=Surface((self.width,self.height))
        self.image.fill((self.col1,self.col2,self.col3))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

#изображения нужные
bg1_img = os.path.join(app_folder, "map.jpg")
bg2_img = os.path.join(app_folder,"bg.jpg")
bg_lobby_img = os.path.join(app_folder,"lobby_bg.png")
play_img = os.path.join(app_folder,"play.png")
quit_img= os.path.join(app_folder,"QUIT.png")

menu_img = os.path.join(app_folder,"menu.png")
player_imgl = os.path.join(app_folder,"pl_left.png")
player_imgr = os.path.join(app_folder,"pl_right.png")
player_imgu = os.path.join(app_folder,"pl_up.png")
player_imgd = os.path.join(app_folder,"pl_down.png")
sett_img = os.path.join(app_folder, "Settings.png")
sett_menu_img = os.path.join(app_folder, "setting_menu.png")

mons_imgl = os.path.join(app_folder,"mons_l.png")
mons_imgr = os.path.join(app_folder,"mons_r.png")
mons_imgu = os.path.join(app_folder,"mons_up.png")
mons_imgd = os.path.join(app_folder,"mons_down.png")
hp_img = os.path.join(app_folder,"heart.png")

#параметры окна
window = display.set_mode((1000, 700))
display.set_caption("Logika-game")

but_menu = transform.scale(image.load(menu_img),(150, 75))
but_play = transform.scale(image.load(play_img),(200, 150))
but_quit = transform.scale(image.load(quit_img),(140, 60))
but_sett = transform.scale(image.load(sett_img),(100, 80))
menu_sett = transform.scale(image.load(sett_menu_img),(450, 500))
background_lbl = transform.scale(image.load(bg_lobby_img),(1000, 700))
background1 = transform.scale(image.load(bg1_img),(1000,700))
background2 = transform.scale(image.load(bg2_img),(1000,700))
heart = transform.scale(image.load(hp_img), (50, 50))
x=0
z=0
rv=0 

#спрайт игрока
hero = Player(player_imgd,player_imgu,player_imgl,player_imgr, 730, 150, 40, 50, 5, 100)

##############################################################################
walls = sprite.Group()
room = []
room2 = []
room3 = []
room4 = []
room5 = []
room6 = []
room7 = []

t1 = Wall(3, 700/700*62, 1000/1000*665, 700/700*307, 255, 0, 0)
t2 = Wall(3, 700/700*55, 1000/1000*335, 700/700*370, 255, 0, 0)
t3 = Wall(1000/1000*55, 3, 1000/1000*148, 700/700*291, 255, 0, 0)
exit_t4 = Wall(1000/1000*63, 5, 1000/1000*460, 700/700*280, 255, 0, 0)
##############################################################################
ch=True
clock=time.Clock()

finish=False
speed_vis = False
health_vis = False
visible = False

click = 0
#Wait - это то чем можно занять цикл, чтобы спрайт продолжал ждать
wait = 0

#monsters
monsters = []

mons_r1 = []
mons_r2 = []
mons_r3 = []
mons_r4 = []
mons_r5 = []
mons_r6 = []
mons_r7 = []
mons_r8 = []

num = randint(1,3)
num2 = randint(1,2)
num3 = randint(2,4)
for i in range(num):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(815, 945), randint(110, 130), 25, 50, 1, 10)
   mons_r1.append(monster)

for i in range(num2):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(830, 975), randint(425, 450), 25, 50, 1, 10)
   mons_r2.append(monster)

for i in range(1):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(245, 320), randint(445, 455), 25, 50, 1, 10)
   mons_r3.append(monster)

for i in range(1):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(135, 215), randint(440, 460), 25, 50, 1, 10)
   mons_r4.append(monster)

for i in range(1):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(25, 110), randint(440, 460), 25, 50, 1, 10)
   mons_r5.append(monster)

for i in range(1):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(224, 232), randint(303, 304), 25, 50, 1, 10)
   mons_r6.append(monster)

for i in range(1):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(31, 50), randint(303, 304), 25, 50, 1, 10)
   mons_r7.append(monster)

for i in range(num3):
   monster = Monster(mons_imgd, mons_imgu, mons_imgl, mons_imgr, randint(33, 312), randint(190, 225), 25, 50, 1, 10)
   mons_r8.append(monster)
#randint(31, 112), win_y/700*(randint(310, 315)
monsters = [mons_r1, mons_r2, mons_r3, mons_r4, mons_r5, mons_r6, mons_r7, mons_r8]

run=True
game="stop"
game_room1 = False
game_room2 = False
game_room3 = False
game_room4 = False
game_room5 = False
game_room6 = False
game_room7 = False
game_room8 = False

#window size
base_font = font.Font(None, 32)
window_x, window_y =  window.get_size()
text = base_font.render("X", True, (0,0,0))
color = (98, 98, 98)

wait_time = 0
up = False
down = False
right = False
left = False

collide = False

while run:
    win_x, win_y = window.get_size()
    win_x1 = int(win_x) - 120
    win_y1 = int(win_y) - 100
    window.blit(background_lbl,(0,0))
    window.blit(but_play, (win_x / 2 - 100, win_y / 2 - 100))
    window.blit(but_quit, (win_x / 2 - 100 + 35, win_y / 2 - 100 + 135))

    if visible == True:
        window.blit(menu_sett, (win_x1 - 220, win_y1 - 420))

        if (win_x, win_y) == (1000, 700):
            input_rect = Rect(820, 350, 50, 32)
            input_rect2 = Rect(890, 350, 50, 32)
        elif (win_x, win_y) == (800, 600):
            input_rect = Rect(win_x1 - 60, win_y1 - 225, 50, 32)
            input_rect2 = Rect(win_x1 + 10, win_y1 - 225, 50, 32)
        elif (win_x, win_y) == (1200, 800):
            input_rect = Rect(win_x1 - 60, win_y1 - 195, 50, 32)
            input_rect2 = Rect(win_x1 + 10, win_y1 - 195, 50, 32)
        elif (win_x, win_y) == (1400, 850):
            input_rect = Rect(win_x1 - 60, win_y1 - 160, 50, 32)
            input_rect2 = Rect(win_x1 + 10, win_y1 - 160, 50, 32)

        draw.rect(window, color, input_rect)
        draw.rect(window, color, input_rect2)

        text_surface = base_font.render(str(window_x), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60, win_y1 - 250 + 5))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 5))
        text_surface2 = base_font.render(str(window_y), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 5))

        text_surface = base_font.render(str(window_x - 200), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60 + 10, win_y1 - 250 + 35))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 35))
        text_surface2 = base_font.render(str(window_y - 100), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 35))

        text_surface = base_font.render(str(window_x + 200), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60, win_y1 - 250 + 65))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 65))
        text_surface2 = base_font.render(str(window_y + 100), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 65))

        text_surface = base_font.render(str(window_x + 400), True, (0, 0, 0))
        window.blit(text_surface, (win_x1 - 60, win_y1 - 250 + 95))
        window.blit(text, (win_x1 - 60 + 52, win_y1 - 250 + 95))
        text_surface2 = base_font.render(str(window_y + 150), True, (0, 0, 0))
        window.blit(text_surface2, (win_x1 + 10, win_y1 - 250 + 95))

    window.blit(but_sett, (win_x1, win_y1))

    #проверка событий
    for e in event.get():
        if e.type==QUIT:
            run=False

        if e.type == MOUSEBUTTONDOWN:
            x, y = mouse.get_pos()
            print(x,y)
            if x >= win_x / 2 - 80 and x <= win_x / 2 + 70:
                if y >= win_y / 2 - 50 and y <= win_y / 2:
                    game='start'
                    speed_vis = True
                    health_vis = True
            if x >= 20 and x <= 130:
                if y >= 15 and y <= 60:
                    game='stop'
                    speed_vis = False
                    health_vis = False
            if x >= win_x / 2 - 65 and x <= win_x / 2 + 70 and game == 'stop':
                if y >= win_y / 2 + 20 and y <= win_y / 2 + 85:
                    run=False
            if x >= win_x1 - 10 and x <= win_x and visible == True:
                if y >= win_y1 + 10 and y <= win_y1 + 70 and visible == True:
                    visible = False 
            elif x >= win_x1 - 10 and x <= win_x and visible == False:
                if y >= win_y1 + 10 and y <= win_y1 + 70 and visible == False:
                    visible = True 

            if x >= win_x - 65 and x <= win_x - 45 and visible == True:
                if y >= win_y1 - 235 and y <= win_y1 - 220 and visible == True:
                    visible2 = True

            elif x >= win_x - 65 and x <= win_x - 45 and visible == True:
                if y >= win_y1 - 235 and y <= win_y1 - 220 and visible == True:
                    visible2 = False
                    
            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 210 and y <= win_y1 - 180 and visible == True:
                    window = display.set_mode((800, 600)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(800, 600))
                    background1 = transform.scale(image.load(bg1_img),(800, 600))
                    background2 = transform.scale(image.load(bg2_img),(800, 600))
                    hero.rect.x, hero.rect.y = ((800 / 1000 * 730), (600 / 700 * 145))
                    t1.kill()
                    t2.kill()
                    t3.kill()
                    exit_t4.kill()
                    t1 = Wall(3, 600/700*62, 800/1000*665, 600/700*307, 255, 125, 0)
                    t2 = Wall(3, 600/700*55, 800/1000*335, 600/700*370, 255, 0, 0)
                    t3 = Wall(800/1000*55, 3, 800/1000*148, 600/700*291, 255, 0, 0)
                    exit_t4 = Wall(800/1000*63, 5, 800/1000*460, 600/700*281, 255, 0, 0)
                    walls.add(t1)
                    walls.add(t2)
                    walls.add(t3)
                    walls.add(exit_t4)

            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 250 and y <= win_y1 - 230 and visible == True:
                    window = display.set_mode((1000, 700)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(1000, 700))
                    background1 = transform.scale(image.load(bg1_img),(1000, 700))
                    background2 = transform.scale(image.load(bg2_img),(1000, 700))
                    hero.rect.x, hero.rect.y = ((1000 / 1000 * 730), (700 / 700 * 145))
                    t1.kill()
                    t2.kill()
                    t3.kill()
                    exit_t4.kill()
                    t1 = Wall(3, 700/700*62, 1000/1000*665, 700/700*307, 255, 0, 0)
                    t2 = Wall(3, 700/700*55, 1000/1000*335, 700/700*370, 255, 0, 0)
                    t3 = Wall(1000/1000*55, 3, 1000/1000*148, 700/700*291, 255, 0, 0)
                    exit_t4 = Wall(1000/1000*63, 5, 1000/1000*460, 700/700*281, 255, 0, 0)
                    walls.add(t1)
                    walls.add(t2)
                    walls.add(t3)
                    walls.add(exit_t4)

            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 190 and y <= win_y1 - 165  and visible == True:
                    window = display.set_mode((1200, 800)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(1200, 800))
                    background1 = transform.scale(image.load(bg1_img),(1200, 800))
                    background2 = transform.scale(image.load(bg2_img),(1200, 800))
                    hero.rect.x, hero.rect.y = ((1200 / 1000 * 730), (800 / 700 * 145))
                    t1.kill()
                    t2.kill()
                    t3.kill()
                    exit_t4.kill()
                    t1 = Wall(3, 800/700*62, 1200/1000*665, 800/700*307, 255, 0, 0)
                    t2 = Wall(3, 800/700*55, 1200/1000*335, 800/700*370, 255, 0, 0)
                    t3 = Wall(1200/1000*55, 3, 1200/1000*148, 800/700*291, 255, 0, 0)
                    exit_t4 = Wall(1200/1000*63, 5, 1200/1000*460, 800/700*281, 255, 0, 0)
                    walls.add(t1)
                    walls.add(t2)
                    walls.add(t3)
                    walls.add(exit_t4)

            if x >= win_x1 - 60 and x <= win_x - 60 and visible == True:
                if y >= win_y1 - 160 and y <= win_y1 - 140  and visible == True:
                    window = display.set_mode((1400, 850)) 
                    background_lbl = transform.scale(image.load(bg_lobby_img),(1400, 850))
                    background1 = transform.scale(image.load(bg1_img),(1400, 850))
                    background2 = transform.scale(image.load(bg2_img),(1400, 850))
                    hero.rect.x, hero.rect.y = ((1400 / 1000 * 730), (850 / 700 * 145))
                    t1.kill()
                    t2.kill()
                    t3.kill()
                    exit_t4.kill()
                    t1 = Wall(3, 850/700*62, 1400/1000*665, 850/700*307, 255, 0, 0)
                    t2 = Wall(3, 850/700*55, 1400/1000*335, 850/700*370, 255, 0, 0)
                    t3 = Wall(1400/1000*55, 3, 1400/1000*148, 850/700*291, 255, 0, 0)
                    exit_t4 = Wall(1400/1000*63, 5, 1400/1000*460, 850/700*281, 255, 0, 0)
                    walls.add(t1)
                    walls.add(t2)
                    walls.add(t3)
                    walls.add(exit_t4)

    #отоброжение комнат и среды
    if game == "start":
        window.blit(background1,(0,0))
        window.blit(but_menu,(0,0))
        visible = False
        visible2 = False

        #walls 
        for i in range(len(room)):
            room[i].kill()
        for i in range(len(room2)):
            room2[i].kill()
        for i in range(len(room3)):
            room3[i].kill()
        for i in range(len(room4)):
            room4[i].kill()
        for i in range(len(room5)):
            room5[i].kill()
        for i in range(len(room6)):
            room6[i].kill()
        for i in range(len(room7)):
            room7[i].kill()

        w1 = Wall(3, win_y/700 * 270, win_x/1000 * 338, win_y/700 * 90, 90, 90, 90)
        w2 = Wall(3, win_y/700 * 90, win_x/1000 * 335, win_y/700 * 425, 90, 90, 90)
        w3 = Wall(3, win_y/700 * 215, win_x/1000*662, win_y/700*90, 90, 90, 90)
        w4 = Wall(3, win_y/700*150, win_x/1000*662, win_y/700*370, 90, 90, 90)
        w5 = Wall(win_x/1000*660, 3, win_x/1000*335, win_y/700*89, 90, 90, 90)
        w6 = Wall(win_x/1000*330, 3, win_x/1000*335, win_y/700*515, 90, 90, 90)
        w7 = Wall(win_x/1000*120, 3, win_x/1000*340, win_y/700*280, 90, 90, 90)
        w8 = Wall(win_x/1000*140, 3, win_x/1000*520, win_y/700*280, 90, 90, 90)
        w9 = Wall(3, win_y/700*135, win_x/1000*793, win_y/700*90, 90, 90, 90)
        w10 = Wall(win_x/1000*125, 3, win_x/1000*793, win_y/700*226, 90, 90, 90)
        w11 = Wall(win_x/1000*15, 3, win_x/1000*976, win_y/700*226, 90, 90, 90)
        w12 = Wall(3, win_y/700*400, win_x/1000*990, win_y/700*90, 90, 90, 90)
        w13 = Wall(win_x/1000*55, 3, win_x/1000*660, win_y/700*382, 90, 90, 90)
        w14 = Wall(win_x/1000*220, 3, win_x/1000*770, win_y/700*382, 90, 90, 90)
        w15 = Wall(3, win_y/700*25, win_x/1000*807, win_y/700*380, 90, 90, 90)
        w16 = Wall(3, win_y/700*23, win_x/1000*807, win_y/700*468, 90, 90, 90)
        w17 = Wall(win_x/1000*325, 3, win_x/1000*667, win_y/700*490, 90, 90, 90)
        w18 = Wall(win_x/1000*130, 3, win_x/1000*18, win_y/700*288, 90, 90, 90)
        w19 = Wall(win_x/1000*120, 3, win_x/1000*215, win_y/700*288, 90, 90, 90)
        w20 = Wall(win_x/1000*322, 3, win_x/1000*13, win_y/700*177, 90, 90, 90)
        w21 = Wall(3, win_y/700*315, win_x/1000*15, win_y/700*177, 90, 90, 90)
        w22 = Wall(win_x/1000*320, 3, win_x/1000*15, win_y/700*490, 90, 90, 90)
        w23 = Wall(win_x/1000*40, 3, win_x/1000*19, win_y/700*358, 90, 90, 90)
        w24 = Wall(win_x/1000*23, 3, win_x/1000*110, win_y/700*358, 90, 90, 90)
        w25 = Wall(3, win_y/700*65, win_x/1000*134, win_y/700*292, 90, 90, 90)
        w26 = Wall(3, win_y/700*70, win_x/1000*212, win_y/700*290, 90, 90, 90)
        w27 = Wall(win_x/1000*35, 3, win_x/1000*215, win_y/700*358, 90, 90, 90)
        w28 = Wall(win_x/1000*30, 3, win_x/1000*305, win_y/700*358, 90, 90, 90)
        w29 = Wall(win_x/1000*36, 3, win_x/1000*19, win_y/700*425, 90, 90, 90)
        w30 = Wall(win_x/1000*48, 3, win_x/1000*107, win_y/700*425, 90, 90, 90)
        w31 = Wall(win_x/1000*55, 3, win_x/1000*204, win_y/700*425, 90, 90, 90)
        w32 = Wall(win_x/1000*32, 3, win_x/1000*308, win_y/700*425, 90, 90, 90)
        w33 = Wall(3, win_y/700*60, win_x/1000*120, win_y/700*430, 90, 90, 90)
        w34 = Wall(3, win_y/700*60, win_x/1000*228, win_y/700*430, 90, 90, 90)

        room = [w1, w2, w3, w4, w5, w6, w7, w8]
        room2 = [w9, w10, w11, w12]
        room3 = [w13, w14, w15, w16, w17]
        room4 = [w18, w19, w20, w21, w22]
        room5 = [w23, w24, w25]
        room6 = [w26, w27, w28]
        room7 = [w29, w30, w31, w32, w33, w34]

        for i in range(len(room)):
            walls.add(room[i])
        for i in range(len(room2)):
            walls.add(room2[i])
        for i in range(len(room3)):
            walls.add(room3[i])
        for i in range(len(room4)):
            walls.add(room4[i])
        for i in range(len(room5)):
            walls.add(room5[i])
        for i in range(len(room6)):
            walls.add(room6[i])
        for i in range(len(room7)):
            walls.add(room7[i])

        if len(mons_r1) != 0 and len(mons_r2) != 0:
            walls.add(t1)
            walls.add(t2)
            walls.add(t3)
            walls.add(exit_t4)
        elif len(mons_r1) == 0 and len(mons_r2) == 0:
            walls.remove(t1)
            walls.remove(t2)
        if len(mons_r3) == 0 and len(mons_r4) == 0 and len(mons_r5) == 0 and len(mons_r6) == 0 and len(mons_r7) == 0:
            walls.remove(t3) 
        a = 0
        for i in monsters:
            if len(i) == 0:
                a += 1
        if a == 8:
            walls.remove(exit_t4)


        walls.draw(window)
        hero.update()
        hero.reset()
        hero.kill()
        #AI
        if hero.rect.x >= (win_x/1000*790) and hero.rect.x <= (win_x/1000*985):
            if hero.rect.y >= (win_y/700*0) and hero.rect.y <= (win_y/700*205):
                game_room1 = True
            else:
                game_room1 = False
        else:
            game_room1 = False

        if hero.rect.x >= (win_x/1000*810) and hero.rect.x <= (win_x/1000*995):
            if hero.rect.y >= (win_y/700*385) and hero.rect.y <= (win_y/700*495):
                game_room2 = True
            else:
                game_room2 = False
        else:
            game_room2 = False

        if hero.rect.x >= (win_x/1000*230) and hero.rect.x <= (win_x/1000*330):
            if hero.rect.y >= (win_y/700*425) and hero.rect.y <= (win_y/700*495):
                game_room3 = True
            else:
                game_room3 = False
        else:
            game_room3 = False

        if hero.rect.x >= (win_x/1000*125) and hero.rect.x <= (win_x/1000*225):
            if hero.rect.y >= (win_y/700*425) and hero.rect.y <= (win_y/700*495):
                game_room4 = True
            else:
                game_room4 = False
        else:
            game_room4 = False

        if hero.rect.x >= (win_x/1000*20) and hero.rect.x <= (win_x/1000*115):
            if hero.rect.y >= (win_y/700*425) and hero.rect.y <= (win_y/700*495):
                game_room5 = True
            else:
                game_room5 = False
        else:
            game_room5 = False

        if hero.rect.x >= (win_x/1000*215) and hero.rect.x <= (win_x/1000*333):
            if hero.rect.y >= (win_y/700*320) and hero.rect.y <= (win_y/700*340):
                game_room6 = True
            else:
                game_room6 = False
        else:
            game_room6 = False
        
        if hero.rect.x >= (win_x/1000*22) and hero.rect.x <= (win_x/1000*128):
            if hero.rect.y >= (win_y/700*320) and hero.rect.y <= (win_y/700*340):
                game_room7 = True
            else:
                game_room7 = False
        else:
            game_room7 = False

        if hero.rect.x >= (win_x/1000*18) and hero.rect.x <= (win_x/1000*338):
            if hero.rect.y >= (win_y/700*150) and hero.rect.y <= (win_y/700*285):
                game_room8 = True
            else:
                game_room8 = False
        else:
            game_room8 = False

        if hero.hp <= 100:
            hero.health()

        if game_room1 == True:
            for i in mons_r1:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r1:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(815, 945)), win_y/700*(randint(125, 130)))

        if game_room2 == True:
            for i in mons_r2:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r2:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(830, 975)), win_y/700*(randint(425, 450)))

        if game_room3 == True:
            for i in mons_r3:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r3:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(245, 320)), win_y/700*(randint(445, 450)))

        if game_room4 == True:
            for i in mons_r4:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r4:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(135, 215)), win_y/700*(randint(440, 450)))

        if game_room5 == True:
            for i in mons_r5:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r5:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(25, 110)), win_y/700*(randint(440, 450 )))

        if game_room6 == True:
            for i in mons_r6:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r6:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(224, 232)), (randint(303, 304)))

        if game_room7 == True:
            for i in mons_r7:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r7:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(31, 50)), (randint(303, 304)))

        if game_room8 == True:
            for i in mons_r8:
                i.reset()
                i.AI()
                i.collide()
        else:
            for i in mons_r8:
                (i.rect.x, i.rect.y) = (win_x/1000*(randint(33, 312)), win_y/700*(randint(190, 225)))


    #проверка столкновений
    if sprite.spritecollide(hero, walls, False):
        collide = True
        if hero.s == 0 or down == True:
            hero.rect.y = hero.rect.y - hero.speed
            
        elif hero.s == 1 or up == True:
            hero.rect.y = hero.rect.y + hero.speed

        elif hero.s == 2 or left == True:
            hero.rect.x = hero.rect.x + hero.speed

        elif hero.s == 3 or right == True:
            hero.rect.x = hero.rect.x - hero.speed
    else:
        collide = False

    if speed_vis == True:
        draw.rect(window, blue, [25, win_y1, 252, 34])
        draw.rect(window, white, [26, win_y1 + 1, 250, 32])
        draw.rect(window, blue, [30, win_y1 + 5, width, 24])

    if health_vis == True:
        draw.rect(window, red, [25, win_y1 - 50, 110, 34])
        draw.rect(window, white, [26, win_y1 - 50 + 1, 108, 32])
        draw.rect(window, red, [30, win_y1 - 50 + 5, width2, 24])
        window.blit(heart, (5, win_y - 160))

    display.update()
    # цикл срабатывает каждую 0.06 секунд
    clock.tick(60)