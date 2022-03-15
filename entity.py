class Entity:
    def __init__(self,x,y,speed):
        self.position = [x,y]
        self.speed = speed

    def move_up(self): self.position[1] -= self.speed
    def move_down(self): self.position[1] += self.speed
    def move_left(self): self.position[0] -= self.speed
    def move_right(self): self.position[0] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom