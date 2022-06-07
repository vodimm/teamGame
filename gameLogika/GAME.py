from pygame import * 
from random import randint
import time as my_time
import os,sys





#----SETTING_GAME----
#player
player_speed=7
player_hp=100

player_size_width, player_size_height = 50,70
FPS=80



#window
display.set_caption('game-Logika')
win_width, win_height = 1200 , 700
window = display.set_mode((win_width, win_height)) 



#COMMON
os.system('cls')
clock = time.Clock()



#----IMG----
#player-stop
img_player_stop=transform.scale(image.load('IMG\player\img_player_down_2.png'), (player_size_width, player_size_height))

#player-up
img_player_up_1=transform.scale(image.load('IMG\player\img_player_up_1.png'), (player_size_width, player_size_height))
img_player_up_2=transform.scale(image.load('IMG\player\img_player_up_2.png'), (player_size_width, player_size_height))
img_player_up_3=transform.scale(image.load('IMG\player\img_player_up_3.png'), (player_size_width, player_size_height))
img_list_player_up=[img_player_up_1,img_player_up_2,img_player_up_1,img_player_up_3]

#player-down
img_player_down_1=transform.scale(image.load('IMG\player\img_player_down_1.png'), (player_size_width, player_size_height))
img_player_down_2=transform.scale(image.load('IMG\player\img_player_down_2.png'), (player_size_width, player_size_height))
img_player_down_3=transform.scale(image.load('IMG\player\img_player_down_3.png'), (player_size_width, player_size_height))
img_list_player_down=[img_player_down_1,img_player_down_2,img_player_down_1,img_player_down_3]

#player-left
img_player_left_1=transform.scale(image.load('IMG\player\img_player_left_1.png'), (player_size_width, player_size_height))
img_player_left_2=transform.scale(image.load('IMG\player\img_player_left_2.png'), (player_size_width, player_size_height))
img_list_player_left=[img_player_left_1,img_player_left_2,img_player_left_1,img_player_left_2]

#player-right
img_player_right_1=transform.scale(image.load('IMG\player\img_player_right_1.png'), (player_size_width, player_size_height))
img_player_right_2=transform.scale(image.load('IMG\player\img_player_right_2.png'), (player_size_width, player_size_height))
img_list_player_right=[img_player_right_1,img_player_right_2,img_player_right_1,img_player_right_2]

#common
img_dark_background='IMG/img_dark_background.png'#dark_background/illusion of light
img_backgraund='IMG/ground_normal.jpg'

#----SOUND----
mixer.init()

mixer.music.load('SOUNDS/sTest-sound.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()


#----CLASS----
class Player(sprite.Sprite):#calss Player and dark_background/illusion of light
    def __init__(self, player_x, player_y):
        sprite.Sprite.__init__(self)

        #player
        self.img_player_now=img_player_stop

        self.player_speed = player_speed

        self.rect = img_player_stop.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.img_number=0
        #dark_background/illusion of light
        self.img_dark_background=transform.scale(image.load(img_dark_background), (win_width*2, win_height*2))

        self.rect_d_b = self.img_dark_background.get_rect()


    def update(self):    
        global values_up, values_down, values_right, values_left
        
        if keys[K_s] and self.rect.y < win_height - player_size_height and values_down == True or keys[K_DOWN] and self.rect.y < win_height -player_size_height:
            self.rect.y += player_speed
            self.img_player_now=img_list_player_down[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0   

        if keys[K_w] and self.rect.y > 5 and values_up == True or keys[K_UP] and self.rect.y > 5:
            self.rect.y -= player_speed
            self.img_player_now=img_list_player_up[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0

        if keys[K_a] and self.rect.x > 5 and values_left == True or keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= player_speed
            self.img_player_now=img_list_player_right[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0

        if keys[K_d] and self.rect.x < win_width - player_size_width and values_right == True or keys[K_RIGHT] and self.rect.x < win_width - player_size_width:
            self.rect.x += player_speed
            self.img_player_now=img_list_player_left[self.img_number]
            self.img_number+=1

        if self.img_number>3:
            self.img_number=0

        if keys[K_d]==keys[K_a]==keys[K_w]==keys[K_s]:
            self.img_player_now=img_player_stop

    def reset(self):
        window.blit(self.img_player_now, (self.rect.x, self.rect.y))
        window.blit(self.img_dark_background, (self.rect.x-win_width+(player_size_width/2), self.rect.y-win_height+(player_size_height/2)))



class Wall(sprite.Sprite):
    def __init__(self, wall_x,wall_y,wall_size_width,wall_size_height):
        sprite.Sprite.__init__(self)

        self.wall_size_width=wall_size_width
        self.wall_size_height=wall_size_height

        self.image=Surface((self.wall_size_width,self.wall_size_height))
        self.image.fill('#000000')

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def update(self):
        window.blit(self.image, (50,50))
        window.blit(self.image, (50,50))



class Enemy(sprite.Sprite):
    def __init__(self, plaer_hp, gun):
        print('calssEnemy')



class Hud(sprite.Sprite):
    def __init__(self, plaer_hp, gun):
        print('classHud')
    #hp
    #guns
    #Inventory / Quick access



class Button(sprite.Sprite):
    def __init__(self,button_img,button_x, button_y, button_size_height,button_size_width,action):
        self.button_x=button_x
        self.button_y=button_y
        self.button_size_height=button_size_height
        self.button_size_width=button_size_width
        self.action=action



class Door():
    def __init__(self, door_x, door_y, door_size_width, door_size_height,tp_x,tp_y,tp_location):
        sprite.Sprite.__init__(self)
        self.door_x=door_x
        self.door_y=door_y
        self.door_size_width=door_size_width
        self.door_size_height=door_size_height
        self.tp_x=tp_x
        self.tp_y=tp_y
        self.tp_location=tp_location

        self.image=Surface((self.door_size_width,self.door_size_height))
        self.image.fill('#FBFF5E')

        self.rect = self.image.get_rect()
        self.rect.x = self.door_x
        self.rect.y = self.door_y


    def update(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
        
    def teleportation(self):
        global location
        player_hero.rect.x=self.tp_x
        player_hero.rect.y=self.tp_y
        location=self.tp_location 


class Book(sprite.Sprite):
    def __init__(self, x,y,):
        self.asdsda=asddasdsa






#----FUNCTION----
def wall_collide(walls_list):
    global values_up, values_down, values_right, values_left
    values_up = values_down = values_right = values_left = True

    #player_hero.rect.y<walls_list[i].rect.y and 
    for i in range(0,len(walls_list)):
        #UP
        if  abs(player_hero.rect.y-(walls_list[i].rect.y+walls_list[i].wall_size_height))<10 and walls_list[i].rect.x-player_size_height< player_hero.rect.x <  (walls_list[i].rect.x+ walls_list[i].wall_size_width):
            values_up=False
        #DOWN
        if  abs((player_hero.rect.y+player_size_height)-walls_list[i].rect.y)<10 and walls_list[i].rect.x-player_size_height< player_hero.rect.x <  (walls_list[i].rect.x+ walls_list[i].wall_size_width):
            values_down=False
        #RIGHT
        if  abs((player_hero.rect.x+player_size_width)-walls_list[i].rect.x)<10 and walls_list[i].rect.y-player_size_height < player_hero.rect.y <  (walls_list[i].rect.y+ walls_list[i].wall_size_height):
            values_right=False
        #LEFT
        if  abs(player_hero.rect.x-(walls_list[i].rect.x+walls_list[i].wall_size_width))<10 and walls_list[i].rect.y-player_size_height < player_hero.rect.y <  (walls_list[i].rect.y+ walls_list[i].wall_size_height):
            values_left=False




def walls_draw(walls_list):
    walls_room_group=sprite.Group()
    for i in range(len(walls_list)):
        walls_room_group.add(walls_list[i])
    walls_room_group.draw(window)










#----OGJECT_GAME----
player_hero=Player(50, 50)
backgraund = transform.scale(image.load(img_backgraund), (win_width, win_height))

door1_room1=Door(500, 500, 50, 50, 50, 50,'location-2')
door1_room2=Door(500, 500, 50, 50, 50, 50,'location-1')






#----ROOMS----
#room-1
#room-1 border


room1_wall1= Wall(0, 0, 550, 20)
room1_wall2= Wall(650, 0, 600, 20)
room1_wall3= Wall(0, 0, 20, 300)
room1_wall4= Wall(0, 400, 20, 300)
room1_wall5= Wall(0, 680, 1200, 20)

room1_wall6= Wall(500, 60, 200, 20)
room1_wall7= Wall(500, 60, 200, 20)


wall_room1_list = [room1_wall1,room1_wall2,room1_wall3,room1_wall4,room1_wall5,room1_wall6,room1_wall7]

#room-2
#room-1 border
room2_wall1= Wall(0, 0, 500, 20)
room2_wall2= Wall(0, 0, 20, 700)
room2_wall3= Wall(700, 0, 30, 20)
room2_wall4= Wall(0, 680, 1200, 20)
room2_wall5= Wall(500, 60, 1000, 20)


wall_room2_list = [room2_wall1,room2_wall2,room2_wall3,room2_wall4,room2_wall5]




#VARIABLE
values_up = values_down = values_right = values_left = True
location='location-1' 
walls_list=wall_room1_list



while True:
    keys = key.get_pressed()

    for e in event.get():
        if e.type==QUIT:
            exit()
    
    if location == 'menu':
        window.fill('#D2D2D2')
        wall_collide(wall_room1_list)
        player_hero.update()
        player_hero.reset()
        walls_draw(wall_room1_list)

    elif location == 'location-1':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room1_list)
        door1_room1.update()
        player_hero.update()
        player_hero.reset()
        walls_draw(wall_room1_list)
        if sprite.collide_rect(door1_room1, player_hero):
            door1_room1.teleportation()
        


    elif location == 'location-2':
        window.blit(backgraund,(0, 0))
        wall_collide(wall_room2_list)
        door1_room2.update()
        player_hero.update()
        player_hero.reset()
        walls_draw(wall_room2_list)
        if sprite.collide_rect(door1_room2, player_hero):
            door1_room2.teleportation()

    display.update()
    clock.tick(FPS)