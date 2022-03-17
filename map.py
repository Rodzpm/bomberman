import dataclasses
from random import randint
from dataclasses import dataclass
import pygame

@dataclass
class Map:
    wall: tuple
    ground: tuple
    block: tuple
    fire: tuple

@dataclass
class Tile:
    type: str
    coor: tuple
    rect: pygame.Rect



class MapManager:
    def __init__(self,case,rate,wall,ground,block,fire):
        #ex 25/13
        self.case = case
        self.rate = rate
        self.sprites = Map(wall,ground,block,fire)
    
    def generate_map(self):
        #générer aléatoirement des cases
        map = []
        for l in range(self.case[1]):
            map.append([])
            for c in range(self.case[0]): 
                if randint(1,self.rate) == 1:
                    map[l].append(Tile("block",(c*40,l*40),pygame.Rect(c*40,l*40,40,40)))
                else:
                    map[l].append(Tile("ground",(c*40,l*40),pygame.Rect(c*40,l*40,40,40)))
        #poser les cases indestructibles
        #bord de la map
        map[0] = [Tile("wall",(i*40,0),pygame.Rect(i*40,0,40,40)) for i in range(len(map[0]))]
        map[-1] = [Tile("wall",(i*40,(self.case[1]-1)*40),pygame.Rect(i*40,(self.case[1]-1)*40,40,40)) for i in range(len(map[0]))]
        for i in range(self.case[1]):
            map[i][0] = Tile("wall",(0,i*40),pygame.Rect(0,i*40,40,40)) 
            map[i][-1] = Tile("wall",((self.case[0]-1)*40,i*40),pygame.Rect((self.case[0]-1)*40,i*40,40,40)) 
        #piliers
        #commence à (2,2) jusqu'à (10,22)
        for l in range(2,self.case[1]-2):
            for c in range(2,self.case[0]-2):
                if l%2 == 0 and c%2 == 0:
                    map[l][c] = Tile("wall",(c*40,l*40),pygame.Rect(c*40,l*40,40,40)) 
        #retirer les cases aux spawn
        map[1][1] = Tile("ground",(40,40),pygame.Rect(40,40,40,40))
        map[2][1] = Tile("ground",(80,40),pygame.Rect(80,40,40,40))
        map[1][2] = Tile("ground",(40,80),pygame.Rect(40,80,40,40))

        map[(self.case[1]-2)][1] = Tile("ground",(40*(self.case[1]-2),40),pygame.Rect(40*(self.case[1]-2),40,40,40))
        map[(self.case[1]-3)][1] = Tile("ground",(40*(self.case[1]-3),40),pygame.Rect(40*(self.case[1]-3),40,40,40))
        map[(self.case[1]-2)][2] = Tile("ground",(40*(self.case[1]-3),80),pygame.Rect(40*(self.case[1]-3),80,40,40))


        map[1][(self.case[0]-2)] = Tile("ground",(40,40*(self.case[0]-2)),pygame.Rect(40,40*(self.case[0]-2),40,40))
        map[1][(self.case[0]-3)] = Tile("ground",(40,40*(self.case[0]-3)),pygame.Rect(40,40*(self.case[0]-3),40,40))
        map[2][(self.case[0]-2)] = Tile("ground",(80,40*(self.case[0]-2)),pygame.Rect(80,40*(self.case[0]-2),40,40))
        
        map[(self.case[1]-2)][(self.case[0]-2)] = Tile("ground",((self.case[1]-2)*40,(self.case[0]-2)*40),pygame.Rect((self.case[1]-2)*40,(self.case[0]-2)*40,40,40))
        map[(self.case[1]-2)][(self.case[0]-3)] = Tile("ground",((self.case[1]-2)*40,(self.case[0]-3)*40),pygame.Rect((self.case[1]-2)*40,(self.case[0]-3)*40,40,40))
        map[(self.case[1]-3)][(self.case[0]-2)] = Tile("ground",((self.case[1]-3)*40,(self.case[0]-2)*40),pygame.Rect((self.case[1]-3)*40,(self.case[0]-2)*40,40,40))
        return map

        

    


