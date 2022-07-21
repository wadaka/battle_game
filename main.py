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

class Sol_1(pygame.sprite.Sprite):
    def __init__(self,x,y,z):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.hp = 1

        self.images = list()
        self.images.append(pygame.image.load("graphic/sol1.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/sol2.png").convert_alpha())
        self.images.append(pygame.image.load("graphic/sol3.png").convert_alpha())


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

        group = pygame.sprite.RenderUpdates()
        Shot_1.containers = group
        Shot_1_Hit.containers = group
        Shot_2.containers = group
        Shot_2_Hit.containers = group

        bg = pygame.image.load("graphic/bg.png").convert_alpha()
        fg = pygame.image.load("graphic/fg.png").convert_alpha()

        rect_fg = fg.get_rect()
        rect_bg = bg.get_rect()

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

        #プレイヤーステータス関連

        while True:
            pygame.display.update()
            clock.tick(FPS)
            #pygame.time.wait(30)
            #screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし

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
                        Shot_2(RETICLE_WIDTH,RETICLE_HEIGHT)
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
                        Shot_1(RETICLE_WIDTH,RETICLE_HEIGHT)
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

            self.screen.blit(bg, rect_bg)
            self.screen.blit(reticle,(RETICLE_WIDTH,RETICLE_HEIGHT))
            group.update()
            group.draw(self.screen)
            self.screen.blit(fg, rect_fg)
            self.screen.blit(txt1 if isShot1_Active == True else txt3, [120, 47] if isShot1_Active == True else [100,54])
            self.screen.blit(txt2 if isShot2_Active == True else txt3, [880, 47] if isShot2_Active == True else [865,54])

game = Game()
game.main()