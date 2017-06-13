import pygame,projectiles,playerobj,pickups,random

class Alien(pygame.sprite.Sprite):
    def __init__(self,player,x,y,dirx,diry):
        """obiekt sprite obcych, wartosci zmiennych statystyk generowana na podstawie poziomu gracza"""
        pygame.sprite.Sprite.__init__(self)
        self.hp=75+(25*player.getLevel())
        self.speed=0.40+(0.05*player.getLevel())
        self.power=45+(5*player.getLevel())
        if 1000-(75*player.getLevel())>=250:
            self.fire_rate=1000-(75*player.getLevel())
        else:
            self.fire_rate=250
        self.x=x
        self.y=y
        self.dirx=dirx
        self.diry=diry
        self.oldtick=pygame.time.get_ticks()
        self.image=pygame.image.load('images/alien.png')
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

    def getHP(self):
        """zwraca wartosc hp (health points)"""
        return self.hp

    def reduceHP(self,amount):
        """zmniejsza wartosc hp (health points) o wartosc podana w argumencie amount"""
        self.hp-=amount

    def shoot(self,projectile_group,player):
        """tworzy obiekt projectile i dodaje go do grupy projectile_group"""
        currtick=pygame.time.get_ticks()
        if currtick-self.oldtick>self.fire_rate:
            if player.getxPosition()-self.x<0:
                nprojectile=projectiles.Projectile(self.power,-5,2,self.x-3,self.y+16)
                projectile_group.add(nprojectile)
            if player.getxPosition()-self.x>0:
                nprojectile=projectiles.Projectile(self.power,5,2,self.x+35,self.y+16)
                projectile_group.add(nprojectile)
            self.oldtick=currtick

    def collisionCheck(self,projectile_group,player):
        """sprawdza czy zaszla kolizja pomiedzy obiektem alien i obiektami z grupy projectile_group, w przypadku kolizji zmniejsza wartosc zmiennej hp obiektu alien i usuwa obiekt z grupy projectile_group z ktorym zaszla kolizja, po czym dodaj punkty do gracza"""
        colprojectile=pygame.sprite.spritecollideany(self,projectile_group)
        if colprojectile:
            if colprojectile.getPtype() != 2:
                self.reduceHP(colprojectile.getPower())
                player.incrScore(colprojectile.getPower())
                colprojectile.kill()

    def movement(self,screen_width,screen_height):
        """nadaje kierunek i predkosc ruchu obiektu alien i dodaje ograniczenia na ramach okna, w przypadku przekroczenia lewej krawedzi okna obiekt zostaje usuniety"""
        self.x+=self.dirx*self.speed
        self.y+=self.diry*self.speed

        if self.y>=screen_height-32:
            self.diry=self.diry*-1
        if self.y<=0:
            self.diry=self.diry*-1
        if self.x<0:
            self.kill()


    def update(self,projectile_group,player,screen_width,screen_height,pickup_group):
        """aktualizuje pozycje oraz sprawdza kolizje i warunki, wedlug ktorych obiekt zostaje usuniety lub nie"""
        self.rect.x=self.x
        self.rect.y=self.y
        self.shoot(projectile_group,player)
        self.collisionCheck(projectile_group,player)
        self.movement(screen_width,screen_height)
        if self.hp<0 or self.hp==0:
            player.addPlayerShield(17.5+(12.5*player.getLevel()))
            player.addCash(30*player.getLevel())
            if random.randint(0,10)>6:
                pickup=pickups.Pickup(random.randint(1,3),self.x,self.y)
                pickup_group.add(pickup)
            self.kill()
