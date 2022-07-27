import pygame
from pygame.locals import *
import random
import time
import sys


# 画面サイズ
SURFACE_WIDTH = 1024
SURFACE_HEIGHT = 600
FPS = 60
walls_1 = [pygame.Rect(140,365,40,60),
            pygame.Rect(170,400,40,35),
            pygame.Rect(430,400,160,20)]
    
walls_2 = [pygame.Rect(45,160,70,190),
        pygame.Rect(130,245,30,110),
        pygame.Rect(170,300,60,60),
        pygame.Rect(900,340,90,20),
        pygame.Rect(940,290,55,50),
        pygame.Rect(975,180,20,130),
        pygame.Rect(950,190,30,15)]

walls_3 = [pygame.Rect(150,240,60,60),
        pygame.Rect(210,265,25,85),
        pygame.Rect(240,290,20,70),
        pygame.Rect(260,320,20,50),
        pygame.Rect(290,350,20,20),
        pygame.Rect(790,340,200,20),
        pygame.Rect(820,310,160,20),
        pygame.Rect(910,290,80,25),
        pygame.Rect(990,220,50,15),
        pygame.Rect(818,245,27,70)]

walls_4 = [pygame.Rect(230,190,105,110),
        pygame.Rect(275,165,65,25),
        pygame.Rect(450,250,108,50),
        pygame.Rect(460,235,100,10),
        pygame.Rect(510,200,40,25),
        pygame.Rect(660,170,70,135),
        pygame.Rect(740,195,25,105)]

ground_1 = [pygame.Rect(0,380,1024,240)]

ground_2 = [pygame.Rect(280,355,520,35)]

ground_3 = [pygame.Rect(280,325,520,30)]

GREEN = (0, 255, 0)

# 自機弾１のクラス
class Shot_1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0
        self.gra_x = 200
        self.gra_y = 200
        self.pos_x = 0
        self.pos_y = 300
        self.go_to_x = x+25
        self.go_to_y = y+25

        self.myrect_1 = pygame.Rect(x,y,50,50)
        self.myrect_2 = pygame.Rect(x+25,y+25,25,25)

        self.image = pygame.image.load("graphic/bullet_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [self.go_to_x,self.go_to_y]

    def dead(self):
        Shot_1_Hit(self.go_to_x,self.go_to_y,0)
        self.kill()

    def update(self):
        self.count += 1

        if self.count == 29:
            if self.myrect_1.collidelist(walls_1) != -1:
                print("walls_1_hit")
                Shot_1_Hit(self.go_to_x,self.go_to_y,0)
                self.kill()
        if self.count == 31:
            if self.myrect_1.collidelist(walls_2) != -1:
                print("walls_2_hit")
                Shot_1_Hit(self.go_to_x,self.go_to_y,0)
                self.kill()
        if self.count == 32:
            if self.myrect_1.collidelist(walls_3) != -1 or self.myrect_1.collidelist(ground_1) != -1:
                print("walls_3_hit")
                Shot_1_Hit(self.go_to_x,self.go_to_y,0)
                self.kill()
        if self.count == 38:
            if self.myrect_1.collidelist(ground_2) != -1:
                print("walls_4_1_hit")
                Shot_1_Hit(self.go_to_x,self.go_to_y,1)
                self.kill()
        if self.count == 39:
            if self.myrect_2.collidelist(walls_4) != -1 or self.myrect_1.collidelist(ground_3) != -1:
                print("walls_4_hit")
                Shot_1_Hit(self.go_to_x,self.go_to_y,2)
                self.kill()

        if self.count == 61:
            print("shot_1_timeout")
            self.kill()

        
        aft_gra_x = self.gra_x - int(5*self.count)
        aft_gra_y = self.gra_y - int(5*self.count)


        if aft_gra_x <= 0:
            aft_gra_x = 1
        if aft_gra_y <= 0:
            aft_gra_y = 1

        if self.count <30:
            aft_pos_x = int(self.go_to_x/30*self.count)
            aft_pos_y = self.pos_y + int((self.go_to_y - self.pos_y)/30*self.count)
            #self.pos_x += aft_pos_x
            #self.pos_y += aft_pos_y
        else:
            aft_pos_x=self.go_to_x
            aft_pos_y=self.go_to_y

        self.image = pygame.transform.smoothscale(self.image,(aft_gra_x,aft_gra_y))
        self.rect = self.image.get_rect()
        self.rect.center = [aft_pos_x,aft_pos_y]
        #self.rect.center = [self.pos_x,self.pos_y]

# 自機弾1命中時のヒットエフェクト用クラス
class Shot_1_Hit(pygame.sprite.Sprite):
    def __init__(self,x,y,z):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0

        self.images = list()
        self.images.append(pygame.image.load("graphic/shot1_hit_0.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/shot1_hit_1.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/shot1_hit_2.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/shot1_hit_3.png").convert_alpha())
        if z == 1:
            for i in range(len(self.images)) :
                self.images[i] = pygame.transform.smoothscale(self.images[i],(70,70))

        if z == 2:
            for i in range(len(self.images)) :
                self.images[i] = pygame.transform.smoothscale(self.images[i],(50,50))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

        self.myrect_1 = pygame.Rect(x,y,50,50)
        self.myrect_2 = pygame.Rect(x+25,y+25,25,25)

    def update(self):

        if self.count % 4 == 0:

            if self.index >= len(self.images):
                self.index = len(self.images)-1
            self.image = self.images[self.index]
            self.index += 1
        
        self.count += 1

        if self.count == 22:
            self.kill()

# 自機弾2のクラス
class Shot_2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0
        self.gra_x = 200
        self.gra_y = 200
        self.pos_x = 1024
        self.pos_y = 300

        self.go_to_x = x+25
        self.go_to_y = y+25

        self.myrect_1 = pygame.Rect(x,y,50,50)
        self.myrect_2 = pygame.Rect(x+25,y+25,25,25)

        self.images = list()
        self.images.append(pygame.image.load("graphic/bullet_3_1.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/bullet_3_2.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/bullet_3_3.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/bullet_3_4.png").convert_alpha())
        self.index = random.randint(0,3)
        self.image = self.images[self.index]

        """
        self.image = pygame.image.load("graphic/bullet_3.png").convert_alpha()
        """
        self.rect = self.image.get_rect()
        self.rect.center = [self.go_to_x,self.go_to_y]
    
    def dead(self):
        Shot_2_Hit(self.go_to_x,self.go_to_y,0)
        self.kill()


    def update(self):
        self.count += 1

        if self.count % 2 ==0:
            if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            self.index += 1

        if self.count == 15:
            if self.myrect_1.collidelist(walls_1) != -1:
                print("walls_1_hit")
                Shot_2_Hit(self.go_to_x,self.go_to_y,0)
                self.kill()
        if self.count == 17:
            if self.myrect_1.collidelist(walls_2) != -1:
                print("walls_2_hit")
                Shot_2_Hit(self.go_to_x,self.go_to_y,0)
                self.kill()
        if self.count == 22:
            if self.myrect_1.collidelist(walls_3) != -1 or self.myrect_1.collidelist(ground_1) != -1:
                print("walls_3_hit")
                Shot_2_Hit(self.go_to_x,self.go_to_y,0)
                self.kill()
        if self.count == 24:
            if self.myrect_2.collidelist(walls_4) != -1 or self.myrect_1.collidelist(ground_2) != -1:
                print("walls_4_hit")
                Shot_2_Hit(self.go_to_x,self.go_to_y,1)
                self.kill()

        if self.count == 30:
            self.kill()

        
        aft_gra_x = self.gra_x - int(10*self.count)
        aft_gra_y = self.gra_y - int(10*self.count)


        if aft_gra_x <= 0:
            aft_gra_x = 1
        if aft_gra_y <= 0:
            aft_gra_y = 1

        if self.count <15:
            aft_pos_x = self.pos_x - int((self.pos_x-self.go_to_x)/15*self.count)
            aft_pos_y = self.pos_y + int((self.go_to_y - self.pos_y)/15*self.count)
            #self.pos_x += aft_pos_x
            #self.pos_y += aft_pos_y
        else:
            aft_pos_x=self.go_to_x
            aft_pos_y=self.go_to_y

        self.image = pygame.transform.smoothscale(self.image,(aft_gra_x,aft_gra_y))
        self.rect = self.image.get_rect()
        self.rect.center = [aft_pos_x,aft_pos_y]
        #self.rect.center = [self.pos_x,self.pos_y]

# 自機弾2命中時のヒットエフェクト用クラス
class Shot_2_Hit(pygame.sprite.Sprite):
    def __init__(self,x,y,z):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0

        self.images = list()
        self.images.append(pygame.image.load("graphic/shot1_hit_0.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/shot1_hit_1.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/shot1_hit_2.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/shot1_hit_3.png").convert_alpha())

        for i in range(len(self.images)) :
            self.images[i] = pygame.transform.smoothscale(self.images[i],(75,75))

        if z == 1:
            for i in range(len(self.images)) :
                self.images[i] = pygame.transform.smoothscale(self.images[i],(45,45))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):

        if self.count % 2 == 0:

            if self.index >= len(self.images):
                self.index = len(self.images)-1
            self.image = self.images[self.index]
            self.index += 1
        
        self.count += 1

        if self.count == 10:
            self.kill()

class Soldier_1(pygame.sprite.Sprite):
    def __init__(self,x,y,pattern):
        pygame.sprite.Sprite.__init__(self,self.containers)

        self.hp = 1
        self.count = 0
        self.pattern = pattern

        self.pos_x = x
        self.pos_y = y

        self.state = "appear"

        self.images_ap = list()
        self.images_def = list()
        self.images_dead = list()

        self.sp_num = 0

        self.image_debug = pygame.Rect(0,0,0,0)

        self.cor_list = []
        self.cor = pygame.Rect(0,0,0,0)

        #登場パターン 1:転がり、2:転がり(逆)、3:遮蔽(左)、4:遮蔽(右)、5:遮蔽(下)
        if self.pattern == 1 or self.pattern == 2:
            for i in range(10):
                img_name = 'graphic/sol_start_{}_{}.png'.format(self.pattern,i+1)
                self.images_ap.append(pygame.image.load(img_name).convert_alpha())
        elif self.pattern == 5:
            for i in range(7,11):
                img_name = 'graphic/sol_start_1_{}.png'.format(i)
                self.images_ap.append(pygame.image.load(img_name).convert_alpha())

        
        #デフォルトパターン
        for i in range(3):
            img_name = 'graphic/sol_default_1_{}.png'.format(i+1)
            self.images_def.append(pygame.image.load(img_name).convert_alpha())

        #死亡パターン
        for i in range(8):
            img_name = 'graphic/sol_dead_1_{}.png'.format(i+1)
            self.images_dead.append(pygame.image.load(img_name).convert_alpha())

        self.index = 0
        self.image = self.images_ap[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x,self.pos_y]

    def appear_01(self):
        if self.count < 82:

            if self.count < 36:
                self.pos_x += 5
            elif self.count < 45:
                self.pos_x += 3
            elif self.count < 58:
                self.pos_x += 2
            elif self.count < 70:
                self.pos_x += 1
            elif self.count >70 and self.count %2 ==0:
                self.pos_x +=1

            if self.count < 10:
                self.pos_y -= 2
            elif self.count < 22:
                self.pos_y -= 1
            elif 24 < self.count < 42 and self.count %3 == 0:
                self.pos_y += 3

            if 22 < self.count < 46:
                self.pos_y += 1
            
        if self.count >= 19:
            if self.count %6 == 0:
                if self.index >= 9:
                    self.index = 0
                    self.count = 0
                    self.state = "default"
                else:
                    if 0 < self.sp_num <= 3:
                        self.sp_num += 1
                    elif self.sp_num > 2:
                        self.sp_num = 0
                    else:
                        self.index += 1
                        self.image = self.images_ap[self.index]

                        if self.index == 5:
                            self.pos_x += 30
                            self.sp_num = 1
        self.rect.center = [self.pos_x,self.pos_y]

        
        if self.index == 0:
            self.cor = pygame.Rect(self.pos_x+2,self.pos_y+22,70,50)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 1:
            self.cor = pygame.Rect(self.pos_x+10,self.pos_y+16,50,75)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 2:
            self.cor = pygame.Rect(self.pos_x+11,self.pos_y+2,40,70)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 3:
            self.cor = pygame.Rect(self.pos_x+22,self.pos_y+12,50,3)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 4:
            self.cor = pygame.Rect(self.pos_x+10,self.pos_y+40,65,45)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 5:
            self.cor = pygame.Rect(self.pos_x+2,self.pos_y+35,45,50)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 6:
            self.cor = pygame.Rect(self.pos_x+2,self.pos_y+30,45,55)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 7:
            self.cor = pygame.Rect(self.pos_x+2,self.pos_y+30,45,65)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 8:
            self.cor = pygame.Rect(self.pos_x+5,self.pos_y+4,50,80)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 9:
            self.cor = pygame.Rect(self.pos_x+5,self.pos_y+4,50,80)
            self.cor.center = [self.pos_x,self.pos_y]

    def appear_02(self):
        if self.count < 82:

            if self.count < 36:
                self.pos_x -= 5
            elif self.count < 45:
                self.pos_x -= 3
            elif self.count < 58:
                self.pos_x -= 2
            elif self.count < 70:
                self.pos_x -= 1
            elif self.count >65 and self.count %2 ==0:
                self.pos_x -=1

            if self.count < 10:
                self.pos_y -= 2
            elif self.count < 22:
                self.pos_y -= 1
            elif 24 < self.count < 42 and self.count %3 == 0:
                self.pos_y += 3

            if 22 < self.count < 46:
                self.pos_y += 1
            
        if self.count >= 19:
            if self.count %6 == 0:
                if self.index >= 9:
                    self.index = 0
                    self.count = 0
                    self.state = "default"
                else:
                    if 0 < self.sp_num <= 3:
                        self.sp_num += 1
                    elif self.sp_num > 2:
                        self.sp_num = 0
                    else:
                        self.index += 1
                        self.image = self.images_ap[self.index]

                        if self.index == 5:
                            self.pos_x -= 20
                            self.sp_num = 1
        self.rect.center = [self.pos_x,self.pos_y]

        
        if self.index == 0:
            self.cor = pygame.Rect(self.pos_x+6,self.pos_y+22,70,50)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 1:
            self.cor = pygame.Rect(self.pos_x+20,self.pos_y+16,50,75)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 2:
            self.cor = pygame.Rect(self.pos_x+29,self.pos_y+2,40,70)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 3:
            self.cor = pygame.Rect(self.pos_x+8,self.pos_y+12,50,3)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 4:
            self.cor = pygame.Rect(self.pos_x+5,self.pos_y+40,65,45)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 5:
            self.cor = pygame.Rect(self.pos_x+23,self.pos_y+35,45,50)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 6:
            self.cor = pygame.Rect(self.pos_x+28,self.pos_y+30,45,55)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 7:
            self.cor = pygame.Rect(self.pos_x+28,self.pos_y+30,45,65)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 8:
            self.cor = pygame.Rect(self.pos_x+5,self.pos_y+4,50,80)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 9:
            self.cor = pygame.Rect(self.pos_x+5,self.pos_y+4,50,80)
            self.cor.center = [self.pos_x,self.pos_y]
        
    def default_01(self):
        if self.index < 3:
            if self.count %6 == 1:
                self.image = self.images_def[self.index]
                self.index += 1
        elif self.count >= 120:
            self.count = 0
            self.state = "attack"
            Warning_ring(self.pos_x,self.pos_y)
        self.cor = pygame.Rect(self.pos_x+5,self.pos_x+14,50,70)
        self.cor.center = [self.pos_x,self.pos_y]

    def attack_01(self):
        if self.index > 1:
            if self.count %6 == 1:
                self.index -= 1
                self.image = self.images_def[self.index]
        if self.count >= 60 and self.count %3 ==0:
            Soldier_mzr(self.pos_x,self.pos_y)
        if self.count >= 60 and self.count % 5==0:
            Damage_effect()
        if self.count >= 120:
            self.count = 0
            self.index = 1
            self.state = "default"
        self.cor = pygame.Rect(self.pos_x+5,self.pos_x+14,50,70)
        self.cor.center = [self.pos_x,self.pos_y]

    def hit(self):
        self.hp -=1
        if self.hp < 1:
            self.state = "dead"
            self.count = 0
            print("しにました～")

    def update(self):
        self.count += 1
        if self.state == "dead":
            self.kill()
        elif self.state == "appear":
            if self.pattern == 1:
                self.appear_01()
            elif self.pattern == 2:
                self.appear_02()
        elif self.state == "default":
            self.default_01()
        elif self.state == "attack":
            self.attack_01()

class Soldier_1_dead(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0

        self.pos_x = x
        self.pos_y = y

        self.images_dead = list()

        #死亡パターン
        for i in range(8):
            img_name = 'graphic/sol_dead_1_{}.png'.format(i+1)
            self.images_dead.append(pygame.image.load(img_name).convert_alpha())

        self.index = 0
        self.image = self.images_dead[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x,self.pos_y]

    def dead(self):
        if self.count <= 160:
            if self.count %12 == 0 and self.index < 7:
                self.index += 1
                self.image = self.images_dead[self.index]
        else:
            self.kill()

    def update(self):
        self.count += 1
        self.dead()

class Soldier_2(pygame.sprite.Sprite):
    def __init__(self,x,y,pattern):
        pygame.sprite.Sprite.__init__(self,self.containers)

        self.hp = 1
        self.count = 0
        self.pattern = pattern

        self.pos_x = x
        self.pos_y = y

        self.state = "appear"

        self.images_ap = list()
        self.images_def = list()
        self.images_dead = list()

        self.sp_num = 0

        self.cor_list = []
        self.cor = pygame.Rect(0,0,0,0)

        #登場パターン 1:遮蔽(下)
        if self.pattern == 1:
            for i in range(7,11):
                img_name = 'graphic/sol_start_1_{}.png'.format(i)
                self.images_ap.append(pygame.image.load(img_name).convert_alpha())

        #デフォルトパターン
        for i in range(3):
            img_name = 'graphic/sol_default_1_{}.png'.format(i+1)
            self.images_def.append(pygame.image.load(img_name).convert_alpha())

        #死亡パターン
        for i in range(8):
            img_name = 'graphic/sol_dead_1_{}.png'.format(i+1)
            self.images_dead.append(pygame.image.load(img_name).convert_alpha())

        self.index = 0
        self.image = self.images_ap[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x,self.pos_y]

    def appear_01(self):
            
        if self.count %6 == 0:
            if self.index >= 3:
                self.index = 0
                self.count = 0
                self.state = "default"
            else:
                self.index += 1
                self.image = self.images_ap[self.index]

        self.rect.center = [self.pos_x,self.pos_y]
        
        if self.index == 0:
            self.cor = pygame.Rect(self.pos_x+2,self.pos_y+30,45,55)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 1:
            self.cor = pygame.Rect(self.pos_x+2,self.pos_y+30,45,65)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 2:
            self.cor = pygame.Rect(self.pos_x+5,self.pos_y+4,50,80)
            self.cor.center = [self.pos_x,self.pos_y]
        elif self.index == 3:
            self.cor = pygame.Rect(self.pos_x+5,self.pos_y+4,50,80)
            self.cor.center = [self.pos_x,self.pos_y]

        
    def default_01(self):
        if self.index < 3:
            if self.count %6 == 1:
                self.image = self.images_def[self.index]
                self.index += 1
        elif self.count >= 160:
            self.count = 0
            self.state = "attack"
            Warning_ring(self.pos_x+10,self.pos_y)
        self.cor = pygame.Rect(self.pos_x+5,self.pos_x+14,50,70)
        self.cor.center = [self.pos_x,self.pos_y]

    def attack_01(self):
        if self.index > 1:
            if self.count %6 == 1:
                self.index -= 1
                self.image = self.images_def[self.index]
        if self.count >= 60 and self.count %3 ==0:
            Soldier_mzr(self.pos_x+10,self.pos_y)
        if self.count >= 60 and self.count % 5==0:
            Damage_effect()
        if self.count >= 120:
            self.count = 0
            self.index = 1
            self.state = "default"
        self.cor = pygame.Rect(self.pos_x+5,self.pos_x+14,50,70)
        self.cor.center = [self.pos_x,self.pos_y]

    def hit(self):
        self.hp -=1
        if self.hp < 1:
            self.state = "dead"
            self.count = 0
            print("しにました～")

    def update(self):
        self.count += 1
        if self.state == "dead":
            self.kill()
        elif self.state == "appear":
            if self.pattern == 1:
                self.appear_01()
        elif self.state == "default":
            self.default_01()
        elif self.state == "attack":
            self.attack_01()

class Soldier_2_dead(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0

        self.pos_x = x
        self.pos_y = y

        self.images_dead = list()

        #死亡パターン
        for i in range(8):
            img_name = 'graphic/sol_dead_1_{}.png'.format(i+1)
            self.images_dead.append(pygame.image.load(img_name).convert_alpha())

        self.index = 0
        self.image = self.images_dead[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x,self.pos_y]

    def dead(self):
        if self.count <= 160:
            if self.count %12 == 0 and self.index < 7:
                self.index += 1
                self.image = self.images_dead[self.index]
        else:
            self.kill()

    def update(self):
        self.count += 1
        self.dead()


class Soldier_mzr(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0

        self.pos_x = x-20
        self.pos_y = y

        self.images_mzr = list()

        rot_rdm = random.randint(0,360)

        #まずるパターン
        for i in range(8):
            img_name = 'graphic/sol_mzr_f_{}.png'.format(i+1)
            img_road = pygame.image.load(img_name).convert_alpha()
            img_rotate = pygame.transform.rotozoom(img_road,rot_rdm,1.0)
            self.images_mzr.append(img_rotate)

        self.index = 0
        self.image = self.images_mzr[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x,self.pos_y]

    def update(self):
        self.count += 1
        if self.count <= 24:
            if self.count %3 == 0 and self.index < 7:
                self.index += 1
                self.image = self.images_mzr[self.index]
        else:
            self.kill()

class Warning_ring(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0

        self.pos_x = x-20
        self.pos_y = y

        self.images = list()

        self.images.append(pygame.image.load('graphic/warning_ring_1.png').convert_alpha())
        self.images.append(pygame.image.load('graphic/warning_ring_2.png').convert_alpha())

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x,self.pos_y]

    def update(self):
        self.count += 1
        if self.count %4 == 0:
            self.index = 1
            self.image = self.images[self.index]
        else:
            self.index = 0
            self.image = self.images[self.index]

        if self.count < 30:
            self.image = pygame.transform.smoothscale(self.images[self.index],(150-self.count*5, 150-self.count*5))
            self.rect = self.image.get_rect()
            self.rect.center = [self.pos_x,self.pos_y]
        else:
            self.kill()

class Damage_effect(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.count = 0

        self.rdm_x = random.randint(30,990)
        self.rdm_y = random.randint(60,470)
        self.rdm_rot = random.randint(0,360)

        self.image = pygame.image.load('graphic/bullet_mark.png').convert_alpha()
        img_rotate = pygame.transform.rotozoom(self.image,self.rdm_rot,1.0)
        self.image = pygame.transform.smoothscale(self.image,(10, 10))

        self.rect = self.image.get_rect()
        self.rect.center = [self.rdm_x,self.rdm_y]

    def update(self):
        self.count += 1
        if self.count == 30:
            self.kill()
        elif self.count <= 6 and self.count %2 == 1:
            self.image = pygame.image.load('graphic/bullet_mark.png').convert_alpha()
            img_rotate = pygame.transform.rotozoom(self.image,self.rdm_rot,1.0)
            self.image = pygame.transform.smoothscale(self.image,(11*self.count, 11*self.count))
            self.rect = self.image.get_rect()
            self.rect.center = [self.rdm_x,self.rdm_y]
        elif self.count == 8:
            self.image = pygame.image.load('graphic/bullet_mark.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [self.rdm_x,self.rdm_y]


class Game():

    def __init__(self) -> None:
        pygame.init()
        #self.bullet_group = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HEIGHT), 0, 32)
        self.screen = pygame.display.get_surface()

    def main(self):
        (RETICLE_WIDTH,RETICLE_HEIGHT) = (512,300)
        pygame.display.set_caption("快楽天 2022年6月号")
        reticle = pygame.image.load("graphic/reticle_2.png").convert_alpha()
        pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()
        font1 = pygame.font.Font(None, 60)
        font2 = pygame.font.Font(None, 45)

        shot1_group = pygame.sprite.RenderUpdates()
        Shot_1.containers = shot1_group
        shot2_group = pygame.sprite.RenderUpdates()
        Shot_2.containers = shot2_group
        group = pygame.sprite.RenderUpdates()
        Shot_1_Hit.containers = group
        Shot_2_Hit.containers = group
        Soldier_mzr.containers = group
        Warning_ring.containers = group
        Damage_effect.containers = group
        enemy_group = pygame.sprite.RenderUpdates()
        Soldier_1.containers = enemy_group
        Soldier_1_dead.containers = enemy_group
        enemy_group_2 = pygame.sprite.RenderUpdates()
        Soldier_2.containers = enemy_group_2
        Soldier_2_dead.containers = enemy_group_2

        self.shot1_num = []
        self.shot2_num = []
        self.soldier_1_num = []
        self.soldier_2_num = []

        bg_1 = pygame.image.load("graphic/bg_1.png").convert_alpha()
        bg_2 = pygame.image.load("graphic/bg_2.png").convert_alpha()
        bg_3 = pygame.image.load("graphic/bg_3.png").convert_alpha()
        bg_4 = pygame.image.load("graphic/bg_4.png").convert_alpha()
        fg = pygame.image.load("graphic/fg.png").convert_alpha()

        rect_fg = fg.get_rect()
        rect_bg = bg_1.get_rect()

        #プレイヤー弾関連
        shot1_max_bullet = 12
        shot1_bullet = 12
        shot2_max_bullet = 60
        shot2_bullet = 60

        isShot1_Active = True
        shot1_reboot_count = 180
        shot1_reboot_timer = 0
        isShot2_Active = True
        shot2_reboot_count = 120
        shot2_reboot_timer = 0
        s2_count = 0

        game_count = 0

        #プレイヤーステータス関連

        while True:
            pygame.display.update()
            clock.tick(FPS)
            game_count += 1
            #pygame.time.wait(30)
            self.screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし

            #txt1_1 = font1.render("{}".format(str(shot1_bullet)).rjust(6) if isShot1_Active == True else "RELOAD".rjust(6), True, GREEN)
            #txt2_1 = font1.render("{}".format(str(shot2_bullet)).rjust(6) if isShot2_Active == True else "RELOAD".rjust(6), True, GREEN)

            txt1 = font1.render("{}".format(str(shot1_bullet)).rjust(6), True, GREEN)
            txt2 = font1.render("{}".format(str(shot2_bullet)).rjust(6), True, GREEN)
            txt3 = font2.render("RELOAD".rjust(6), True, GREEN)

            if isShot1_Active == False:
                shot1_reboot_timer -= 1
                if shot1_reboot_timer == 0:
                    isShot1_Active = True
                    shot1_bullet = shot1_max_bullet
            if isShot2_Active == False:
                shot2_reboot_timer -= 1
                if shot2_reboot_timer == 0:
                    isShot2_Active = True
                    shot2_bullet = shot2_max_bullet

            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[2]:
                if isShot2_Active == True:
                    if s2_count == 0:
                        s2_count += 1
                        shot2_bullet -= 1
                        self.shot2_num.append(Shot_2(RETICLE_WIDTH,RETICLE_HEIGHT))
                        if shot2_bullet == 0:
                            isShot2_Active = False
                            shot2_reboot_timer = shot2_reboot_count
                    elif s2_count < 5:
                        s2_count += 1
                    else:
                        s2_count = 0
            else:
                s2_count = 0

            for event in pygame.event.get():

                if event.type == MOUSEMOTION:
                    RETICLE_WIDTH, RETICLE_HEIGHT = event.pos
                    RETICLE_WIDTH -= int(reticle.get_width()/2)
                    RETICLE_HEIGHT -= int(reticle.get_height()/2)

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if isShot1_Active == True:
                        shot1_bullet -= 1
                        self.shot1_num.append(Shot_1(RETICLE_WIDTH,RETICLE_HEIGHT))
                        if shot1_bullet == 0:
                            isShot1_Active = False
                            shot1_reboot_timer = shot1_reboot_count

                if event.type == KEYDOWN:
                    if event.key == K_q:
                        if isShot1_Active == True:
                            isShot1_Active = False
                            shot1_reboot_timer = shot1_reboot_count
                if event.type == KEYDOWN:
                    if event.key == K_e:
                        if isShot2_Active == True:
                            isShot2_Active = False
                            shot2_reboot_timer = shot2_reboot_count
                
                #if event.type == MOUSEBUTTONDOWN and event.button == 3:
                #if event.type == mouse_pressed[2] and event.button == 3:
                    #Shot_2(RETICLE_WIDTH,RETICLE_HEIGHT)
                    #print ("処理を開始します")

            
                if event.type == QUIT:  # 閉じるボタンが押されたら終了
                    pygame.quit()       # Pygameの終了(画面閉じられる)
                    sys.exit()

                if event.type == KEYDOWN:       # キーを押したとき
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()
                
            #shot1_collison = pygame.sprite.groupcollide(shot1_group,enemy_group,False,True)
            #for i in shot1_collison:
                #if self.i.self.count

            for i in reversed(range(len(self.shot1_num))):
                if self.shot1_num[i].count == 28:
                    print("shot1、判定実行")
                    for j in reversed(range(len(self.soldier_1_num))):
                        if self.soldier_1_num[j].cor.colliderect(self.shot1_num[i].myrect_1) == True:
                            print("shot2、命中")
                            self.shot1_num[i].dead()
                            self.soldier_1_num[j].hit()
                            del self.shot1_num[i]

                            if self.soldier_1_num[j].state == "dead":
                                print("へいし、志望")
                                Soldier_1_dead(self.soldier_1_num[j].pos_x,self.soldier_1_num[j].pos_y)
                                del self.soldier_1_num[j]
                            break
                elif self.shot1_num[i].count == 30:
                    print("shot1、判定実行")
                    for j in reversed(range(len(self.soldier_2_num))):
                        if self.soldier_2_num[j].cor.colliderect(self.shot1_num[i].myrect_1) == True:
                            print("shot2、命中")
                            self.shot1_num[i].dead()
                            self.soldier_2_num[j].hit()
                            del self.shot1_num[i]

                            if self.soldier_2_num[j].state == "dead":
                                print("へいし、志望")
                                Soldier_2_dead(self.soldier_2_num[j].pos_x,self.soldier_2_num[j].pos_y)
                                del self.soldier_2_num[j]
                            break

            for i in reversed(range(len(self.shot2_num))):
                if self.shot2_num[i].count == 14:
                    print("shot2、判定実行")
                    for j in reversed(range(len(self.soldier_1_num))):
                        #if self.shot2_num[i].myrect_1.collidelist(self.soldier_1_num[j].cor) != -1:
                        if self.soldier_1_num[j].cor.colliderect(self.shot2_num[i].myrect_1) == True:
                            print("shot2、命中")
                            self.shot2_num[i].dead()
                            self.soldier_1_num[j].hit()
                            del self.shot2_num[i]

                            if self.soldier_1_num[j].state == "dead":
                                print("へいし、志望")
                                Soldier_1_dead(self.soldier_1_num[j].pos_x,self.soldier_1_num[j].pos_y)
                                del self.soldier_1_num[j]
                            break
                elif self.shot2_num[i].count == 16:
                    print("shot2、判定実行")
                    for j in reversed(range(len(self.soldier_2_num))):
                        #if self.shot2_num[i].myrect_1.collidelist(self.soldier_1_num[j].cor) != -1:
                        if self.soldier_2_num[j].cor.colliderect(self.shot2_num[i].myrect_1) == True:
                            print("shot2、命中")
                            self.shot2_num[i].dead()
                            self.soldier_2_num[j].hit()
                            del self.shot2_num[i]

                            if self.soldier_2_num[j].state == "dead":
                                print("へいし、志望")
                                Soldier_2_dead(self.soldier_2_num[j].pos_x,self.soldier_2_num[j].pos_y)
                                del self.soldier_2_num[j]
                            break
            if game_count == 300:
                #Soldier_1(160,380,1)
                #self.soldier_1_num.append(Soldier_1(200,380,1))
                self.soldier_1_num.append(Soldier_1(20,400,1))
            
            if game_count == 360:
                self.soldier_1_num.append(Soldier_1(1084,400,2))

            if game_count == 420:
                self.soldier_2_num.append(Soldier_2(510,360,1))

            #if len(self.soldier_1_num) <1 and game_count % 300 == 0:
                #self.soldier_1_num.append(Soldier_1(20,400,1))

            if len(self.soldier_1_num) <1 and game_count % 360 == 0:
                self.soldier_1_num.append(Soldier_1(1084,400,2))
            
            if len(self.soldier_2_num) <1 and game_count % 420 == 0:
                self.soldier_2_num.append(Soldier_2(510,360,1))


            self.screen.blit(bg_4, rect_bg)
            self.screen.blit(bg_3, rect_bg)
            self.screen.blit(bg_2, rect_bg)

            enemy_group_2.update()
            enemy_group_2.draw(self.screen)

            self.screen.blit(bg_1, rect_bg)

            enemy_group.update()
            enemy_group.draw(self.screen)

            shot1_group.update()
            shot1_group.draw(self.screen)
            shot2_group.update()
            shot2_group.draw(self.screen)
            group.update()
            group.draw(self.screen)

            self.screen.blit(reticle,(RETICLE_WIDTH,RETICLE_HEIGHT))
            self.screen.blit(fg, rect_fg)
            self.screen.blit(txt1 if isShot1_Active == True else txt3, [120, 47] if isShot1_Active == True else [100,54])
            self.screen.blit(txt2 if isShot2_Active == True else txt3, [880, 47] if isShot2_Active == True else [865,54])

game = Game()
game.main()
