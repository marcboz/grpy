import pygame,projectiles,playerobj

class Alien(pygame.sprite.Sprite):
    def __init__(self,hp,speed,power,fr,x,y,dirx,diry):
        pygame.sprite.Sprite.__init__(self)
        self.hp=hp
        self.speed=speed
        self.power=power
        self.fire_rate=fr
        self.x=x
        self.y=y
        self.dirx=dirx
        self.diry=diry
        self.oldtick=pygame.time.get_ticks()
        self.image=pygame.image.load('images/alien.png')
        self.image.convert()
        self.rect=self.image.get_rect()

    def getxPosition(self):
        return self.x

    def getyPostion(self):
        return self.y

    def setPosition(self,x,y):
        self.x=x
        self.y=y

    def getHP(self):
        return self.hp

    def reduceHP(self,amount):
        self.hp-=amount

    def shoot(self,projectile_group,player):
        currtick=pygame.time.get_ticks()
        if currtick-self.oldtick>self.fire_rate:
            if player.getxPosition()-self.x<0:
                nprojectile=projectiles.Projectile(self.power,-5,2,self.x-3,self.y+16)
                projectile_group.add(nprojectile)
            if player.getxPosition()-self.x>0:
                nprojectile=projectiles.Projectile(self.power,5,2,self.x+35,self.y+16)
                projectile_group.add(nprojectile)
            self.oldtick=currtick
            print("pewpew")

    def collisionCheck(self,projectile_group):
        colprojectile=pygame.sprite.spritecollideany(self,projectile_group)
        if colprojectile:
            if colprojectile.getPtype() != 2:
                self.reduceHP(colprojectile.getPower())
                colprojectile.kill()

    def movement(self,screen_width,screen_height):
        self.x+=self.dirx*self.speed
        self.y+=self.diry*self.speed

        if self.y>screen_height:
            self.diry=self.diry*-1
        if self.y+32<0:
            self.diry=self.diry*-1
        if self.x<0:
            self.kill()


    def update(self,projectile_group,player,screen_width,screen_height):
        self.rect.x=self.x
        self.rect.y=self.y
        self.shoot(projectile_group,player)
        self.collisionCheck(projectile_group)
        self.movement(screen_width,screen_height)
        if self.hp<0 or self.hp==0:
            self.kill()
