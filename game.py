from map import MapManager
from player import Player
from object import Object
import pygame

class Game:
    def __init__(self,res):
        #écran et nom du jeu
        self.res = res
        self.screen = pygame.display.set_mode((res[0]*40,res[1]*40))
        pygame.display.set_caption("Bomberman - Python Edition")

        pygame.mixer.init()
        pygame.mixer.set_num_channels(3)
        self.explosion = pygame.mixer.Sound("explosion.ogg")
        self.gamemusic = pygame.mixer.Sound("game.ogg")
        self.gameover = pygame.mixer.Sound("gameover.ogg")
        self.canal_1 = pygame.mixer.Channel(0)
        self.canal_2 = pygame.mixer.Channel(1)
        self.canal_3 = pygame.mixer.Channel(2)

        self.canal_1.play(self.gamemusic,-1)

        #bool pour faire tourner le jeu
        self.running = True
        #clock pour les fps
        self.clock = pygame.time.Clock()
        #map du jeu
        self.map = MapManager(res,5,(175, 175, 175),(34, 120, 15),(127, 127, 127),(255,0,0))
        self.gen_map = self.map.generate_map()
        #joueur
        self.player = Player((50,50),pygame.image.load("player_1.png").convert_alpha(),4)
        #joueur2
        self.player2 = Player((res[0]*40-80,res[1]*40-80),pygame.image.load("player_2.png").convert_alpha(),4)
        #liste avec tous les objets présents sur le jeu
        self.obj_list = []
        self.bomb = pygame.image.load("bomb.png").convert_alpha()
        self.rectBomb = self.bomb.get_rect()
        #charging
        self.charging = False
        #post_explosion
        self.post_explo =0
        #win
        self.win1 = False
        self.win2 = False

    def draw(self):
        #affiche la carte
        for l in range(len(self.gen_map)):
            for c in range(len(self.gen_map[l])):
                o = self.gen_map[l][c]
                if o.type == "ground":
                    pygame.draw.rect(self.screen,self.map.sprites.ground,(c*40,l*40,40,40))
                elif o.type == "block":
                    pygame.draw.rect(self.screen,self.map.sprites.block,(c*40,l*40,40,40))
                elif o.type == "wall":
                    pygame.draw.rect(self.screen,self.map.sprites.wall,(c*40,l*40,40,40))
                elif o.type == "fire":
                    if self.post_explo < 60:
                        pygame.draw.rect(self.screen,self.map.sprites.fire,(c*40,l*40,40,40))
                    else:
                        o.type = "ground"
                        pygame.draw.rect(self.screen,self.map.sprites.ground,(c*40,l*40,40,40))
                        
        #affiche les objets
        for obj in self.obj_list:
            #pygame.draw.rect(self.screen,obj.sprite,(obj.x,obj.y,obj.width,obj.height))
            self.screen.blit(self.bomb,self.rectBomb)
            self.rectBomb.topleft = (obj.x-8,obj.y-8)
        #affiche le joueur
        self.screen.blit(self.player.sprite,self.player.rect)
        self.player.rect.topleft = (self.player.x,self.player.y)
        #affiche le joueur2
        self.screen.blit(self.player2.sprite,self.player2.rect)
        self.player2.rect.topleft = (self.player2.x,self.player2.y)
        #pygame.draw.rect(self.screen,self.player.sprite,(self.player.x,self.player.y,20,20))

        if self.win1:
            win = pygame.image.load("win1.png").convert_alpha()
            self.screen.blit(win,(350,150))
        elif self.win2:
            win = pygame.image.load("win2.png").convert_alpha()
            self.screen.blit(win,(350,150))

    def handle_inputs(self,key_list,player):
        pressed = pygame.key.get_pressed()
        if pressed[key_list[0]]:
            player.move_up()  
        elif pressed[key_list[1]]:
            player.move_down()  
        elif pressed[key_list[2]]:
            player.move_left() 
        elif pressed[key_list[3]]:
            player.move_right() 
        elif pressed[key_list[4]] and not self.charging:
            self.obj_list.append(Object((0,0,255),(player.x//40*40+15,player.y//40*40+15),10,10,self.res))
            print(self.obj_list[-1].x,self.obj_list[-1].y)
            self.charging = True

    def verif_coll(self,player):
        for l in range(len(self.gen_map)):
            for c in range(len(self.gen_map[0])):
                obj = self.gen_map[l][c]
                if obj.type in ["wall","block"] and obj.rect.colliderect(player.rect):
                    player.x = player.temp_pos[0]
                    player.y = player.temp_pos[1]
                    player.update()
                elif obj.type == "fire" and obj.rect.colliderect(player.rect):
                    if self.win1 == False and self.win2 == False:
                        self.canal_1.stop()
                        self.canal_3.play(self.gameover,0)
                    if player == self.player:
                        self.win2 = True
                    else:
                        self.win1 = True
                    
    def obj_event(self):
        for obj in self.obj_list:
            if obj.frame == 120:
                explosion_list = obj.explosion()
                self.canal_2.play(self.explosion,0)
                for tile in explosion_list:
                    print(tile[1],tile[0])
                    if self.gen_map[tile[1]][tile[0]].type in ["ground","block"]:
                        self.gen_map[tile[1]][tile[0]].type = "fire"
                self.obj_list.remove(obj)
                self.charging = False
            else:
                obj.frame += 1
        if self.post_explo < 60:
            self.post_explo += 1
        else:
            self.post_explo = 0


    def update(self):
        self.player.temp_pos = self.player.save_location()
        self.player2.temp_pos = self.player2.save_location()
        self.handle_inputs([pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_RETURN],self.player)
        self.handle_inputs([pygame.K_z,pygame.K_s,pygame.K_q,pygame.K_d,pygame.K_SPACE],self.player2)
        self.player.update()
        self.player2.update()
        self.obj_event()
        self.verif_coll(self.player)
        self.verif_coll(self.player2)
        self.draw()

    def run(self):
        while self.running:
            #update des objets du jeu
            self.update()
            #events appui de touches
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #met à jour l'écran du jeu
            pygame.display.flip()
            self.clock.tick(60)
            


#carte = 25/13