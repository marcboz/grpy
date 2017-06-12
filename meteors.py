import pygame,playerobj

class Meteor(pygame.sprite.Sprite):
    def __init__(self,speed,x,y,dirx,diry):
        pygame.sprite.Sprite.__init__(self)
        self.speed=speed
        self.x=x
        self.y=y
        self.dirx=dirx
        self.diry=diry
        self.image=pygame.image.load('images/meteor.png')
        self.image.convert()
        self.rect=self.image.get_rect()

    def getxPosition(self):
        return self.x

    def getyPostion(self):
        return self.y

    def setPosition(self,x,y):
        self.x=x
        self.y=y

    def collisionCheck(self,player):
        collision=pygame.sprite.collide_rect(self,player)
        if collision:
            player.reducePlayerHP(100)
            self.kill()

    def movement(self,screen_width,screen_height):
        self.x+=self.dirx*self.speed
        self.y+=self.diry*self.speed

        if self.y>screen_height:
            self.kill()
        if self.y+32<0:
            self.kill()
        if self.x<0:
            self.kill()
        


    def update(self,player,screen_width,screen_height):
        self.rect.x=self.x
        self.rect.y=self.y
        self.collisionCheck(player)
        self.movement(screen_width,screen_height)
