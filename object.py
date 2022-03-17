class Object:
    def __init__(self,sprite,pos,width,height,res):
        self.x = pos[0]
        self.y = pos[1]
        self.xa = self.x//40
        self.ya = self.y//40
        self.sprite = sprite
        self.width = width
        self.height = height
        self.res = res
        self.frame = 0

    def explosion(self):
        explosion_list = [(self.xa,self.ya),(self.xa+1,self.ya),(self.xa-1,self.ya),(self.xa,self.ya-1),(self.xa,self.ya+1)]
        return explosion_list
        

