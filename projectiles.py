import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self,pwr,nspeed,ptype,xpos,ypos):
        """obiek sprite pociskow"""
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
        """sprawdza czy zaszla kolizja pomiedzy obiektami grup projectile_group i alien_group oraz obiektami grupy projectile_group i obiektem player (gracz)"""
        colalien=pygame.sprite.spritecollideany(self,alien_group)
        if colalien and self.type==1:
            colalien.reduceHP(self.power)
            player.incrScore(self.power)
            self.kill()
        if pygame.sprite.collide_rect(self,player) and self.type==2:
            player.reducePlayerHP(self.power)
            self.kill()

    def update(self,scrw,alien_group,player):
        """aktualizuje obiekt pocisku"""
        self.x+=self.speed
        self.rect.x=self.x+16
        self.rect.y=self.y+16
        if self.x>scrw or self.x<0:
            self.kill()
        self.collisionCheck(alien_group,player)

    def getPower(self):
        """zwraca wartosc power (sila pocisku)"""
        return self.power;

    def getPtype(self):
        """zwraca typ pocisku"""
        return self.type
