import pygame,playerobj

class Meteor(pygame.sprite.Sprite):
    def __init__(self,speed,x,y,dirx,diry):
        """obiekt sprite asteroid"""
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
        """zwraca pozycje x"""
        return self.x

    def getyPostion(self):
        """zwraca pozycje y"""
        return self.y

    def setPosition(self,x,y):
        """zmienia pozycje x i y"""
        self.x=x
        self.y=y

    def collisionCheck(self,player):
        """sprawdza czy nie zaszla kolizja pomiedzy obiektem asteroidy i gracza i w zaleznosci od tego usuwa obiekt asteroidy"""
        collision=pygame.sprite.collide_rect(self,player)
        if collision:
            player.reducePlayerHP(100)
            self.kill()

    def movement(self,screen_width,screen_height):
        """zmienia wartosc polozenia x i y w zaleznosci od wartosci speed(predkosc)"""
        self.x+=self.dirx*self.speed
        self.y+=self.diry*self.speed

        if self.y>screen_height:
            self.kill()
        if self.y+32<0:
            self.kill()
        if self.x<0:
            self.kill()



    def update(self,player,screen_width,screen_height):
        """aktualizuje obiekt asteroidy"""
        self.rect.x=self.x
        self.rect.y=self.y
        self.collisionCheck(player)
        self.movement(screen_width,screen_height)
