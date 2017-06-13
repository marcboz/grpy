import pygame,playerobj

class Pickup(pygame.sprite.Sprite):
    def __init__(self,ptype,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.ptype=ptype
        self.x=x
        self.y=y

        if self.ptype==1:
            self.amount=100
            self.image=pygame.image.load('images/cpick.png')
            self.image.convert()
            self.rect=self.image.get_rect()

        if self.ptype==2:
            self.image=pygame.image.load('images/hppick.png')
            self.image.convert()
            self.rect=self.image.get_rect()

        if self.ptype==3:
            self.amount=50
            self.image=pygame.image.load('images/shpick.png')
            self.image.convert()
            self.rect=self.image.get_rect()

    def update(self,player):
        self.rect.x=self.x
        self.rect.y=self.y

        if pygame.sprite.collide_rect(self,player):
            if self.ptype==1:
                player.addCash(self.amount)
                self.kill()

            if self.ptype==2:
                player.refillHP()
                self.kill()

            if self.ptype==3:
                player.addPlayerShield(self.amount)
                self.kill()
