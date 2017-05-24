import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self,pwr,nspeed,ptype,xpos,ypos):
        pygame.sprite.Sprite.__init__(self)
        self.power=pwr
        self.speed=nspeed
        self.type=ptype
        self.x=xpos
        self.y=ypos
        if int(ptype)==1:
            self.image=pygame.image.load('images/projectile1.png')
        elif int(ptype)==2:
            self.image=pygame.image.load('images/projectile2.png')

        self.image.convert()
        self.rect=self.image.get_rect()

    def collisionCheck(self,alien_group,player):
        colalien=pygame.sprite.spritecollideany(self,alien_group)
        if colalien and self.type==1:
            colalien.reduceHP(self.power)
            player.incrScore(self.power)
            self.kill()
        if pygame.sprite.collide_rect(self,player) and self.type==2:
            player.reducePlayerHP(self.power)
            self.kill()

    def update(self,scrw,alien_group,player):
        self.x+=self.speed
        self.rect.x=self.x+16
        self.rect.y=self.y+16
        if self.x>scrw or self.x<0:
            self.kill()
        self.collisionCheck(alien_group,player)

    def getPower(self):
        return self.power;

    def getPtype(self):
        return self.type
