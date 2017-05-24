import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,xpos,ypos,hp,speed):
        pygame.sprite.Sprite.__init__(self)
        self.hp=hp
        self.speed=speed
        self.level=1
        self.lvl_up_requirement=self.level*500
        self.score=0
        self.x=xpos
        self.y=ypos
        self.image=pygame.image.load('images/player.png')
        self.image.convert()
        self.rect=self.image.get_rect()


    def getLevel(self):
        return self.level

    def setLevel(self,newlevel):
        self.level=newlevel

    def levelUp(self):
        if self.score==self.lvl_up_requirement:
            self.level+=1

    def getxPosition(self):
        return self.x

    def getyPosition(self):
        return self.y

    def setPosition(self,newx,newy):
        self.x=newx
        self.y=newy

    def getPlayerHP(self):
        return self.hp

    def setPlayerHP(self,newhp):
        self.hp=newhp

    def reducePlayerHP(self,amount):
        self.hp-=amount

    def getPlayerSpeed(self):
        return self.speed

    def setPlayerSpeed(self,newspeed):
        self.speed=newspeed

    def movement(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_s]:
            self.y += self.speed
        elif key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed
        elif key[pygame.K_a]:
            self.x -= self.speed

    def incrScore(self,amount):
        self.score+=amount

    def getScore(self):
        return self.score

    def update(self):
        self.movement()
        self.rect.x=self.x
        self.rect.y=self.y
        if self.hp == 0 or self.hp<0:
            self.kill()
