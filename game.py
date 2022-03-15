import pygame
from entity import Entity
from map import MapGenerator

class Game:
    def __init__(self):
        #boucle du jeu
        self.running = True
        #faire apparaître joueur
        self.is_playing = True
        #creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Bomberman")
        self.clock = pygame.time.Clock()
        self.player = Entity(100,100,4)
        self.map = MapGenerator(800,800,10,3)
        self.gen = self.map.generate_map()

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()  
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()  
        elif pressed[pygame.K_LEFT]:
            self.player.move_left() 
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right() 

    def update(self):
        for i in range(len(self.gen)):
            for j in range(len(self.gen[i])):
                if self.gen[i][j] == 1:
                    pygame.draw.rect(self.screen, (128,128,128), (i*self.map.block_size[0],j*self.map.block_size[1],self.map.block_size[0],self.map.block_size[1]))
        if self.is_playing:
            pygame.draw.rect(self.screen, (255,0,0), (self.player.position[0],self.player.position[1],50,50))
        pygame.display.flip()


    def run(self):
        while self.running:
            #self.update()
            self.handle_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((9, 106, 9))
            self.update()
            self.clock.tick(60)