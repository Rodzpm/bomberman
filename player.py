import pygame

class Player:
    def __init__(self,pos,sprite,speed):
        self.x = pos[0]
        self.y = pos[1]
        self.sprite = sprite
        self.speed = speed
        self.rect = pygame.Rect(self.x,self.y,30,30)
        self.temp_pos = self.save_location()
    
    def move_up(self) : self.y -= self.speed
    def move_down(self) : self.y += self.speed
    def move_left(self) : self.x -= self.speed
    def move_right(self) : self.x += self.speed

    def update(self):
        self.rect = pygame.Rect(self.x,self.y,30,30)
    
    def save_location(self):
        return (self.x,self.y)
    

