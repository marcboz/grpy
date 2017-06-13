import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,xpos,ypos,speed):
        """obiekt sprite gracza, wartosci zmiennych statystyk generowana na podstawie poziomu gracza"""
        pygame.sprite.Sprite.__init__(self)
        self.hp=100
        self.shield=50
        self.level=1
        self.shield_capacity=25+(25*self.level)
        self.speed=speed
        self.lvl_up_requirement=self.level*500
        self.score=0
        self.cash=0
        self.power=50
        self.x=xpos
        self.y=ypos
        self.image=pygame.image.load('images/player.png')
        self.image.convert()
        self.rect=self.image.get_rect()


    def getLevel(self):
        """zwraca level (poziom) gracza"""
        return self.level

    def levelUp(self):
        """zwieksza poziom gracza o 1 w przypadku gdy score (wynik) osiadnie lvl_up_requirement (warosc score wymagana do nastepnego poziomu)"""
        if self.score>=self.lvl_up_requirement:
            self.level+=1
            self.lvl_up_requirement=self.level*500
            self.hp=75+self.level*25
            self.shield=25+self.level*25

    def getxPosition(self):
        """zwraca pozycje x"""
        return self.x

    def getyPosition(self):
        """zwraca pozycje y"""
        return self.y

    def setPosition(self,newx,newy):
        """zmienia pozycje x i y"""
        self.x=newx
        self.y=newy

    def getPlayerHP(self):
        """zwraca wartosc hp (health points)"""
        return self.hp

    def getPlayerShield(self):
        """zwraca wartosc shield (tarcza)"""
        return self.shield

    def addPlayerShield(self,amount):
        """dodaje punkty shield (tarczy) o wartosc argumentu amount do osiagniecia limitu (shield_capacity)"""
        if self.shield+amount>self.shield_capacity:
            self.shield=self.shield_capacity
        else:
            self.shield+=amount

    def reducePlayerHP(self,amount):
        """zmniejsza wartosc tarczy o wartosc amount, a w przypadku gdy wartosc tarczy jest mniejsza od argumentu amount roznica amount i shield zostaje odjeta od wartosci hp (health points)"""
        if self.shield<amount:
            self.hp-=amount-self.shield
            self.shield=0
        if self.shield>=amount:
            self.shield-=amount

    def getPlayerSpeed(self):
        """zwraca wartosc speed (predkosc)"""
        return self.speed

    def setPlayerSpeed(self,newspeed):
        """zmienia wartosc speed(predkosc)"""
        self.speed=newspeed

    def getPlayerCash(self):
        """zwraca wartosc cash (pieniadze)"""
        return self.cash

    def addCash(self,amount):
        """zwieksza wartosc cash o wartosc argumentu amount"""
        self.cash+=amount

    def reduceCash(self,amount):
        """zmniejsza wartosc cash o wartosc argumentu amount"""
        self.cash-=amount

    def refillHP(self):
        """ustawia maksymalne hp (health points) w zaleznosci od zmiennej level (poziom)"""
        self.hp=75+self.level*25

    def upgradeShield(self):
        """zwieksza limit tarczy o 50"""
        self.shield_capacity+=50

    def getPlayerPower(self):
        """zwraca wartosc power (sila pocisku)"""
        return self.power

    def upgradeWeapon(self):
        """zwieksza wartosc power o 25"""
        self.power+=25

    def movement(self,screen_width,screen_height):
        """zmienia pozycje x i y w zaleznosci od zmiennych speed i ograniczen na ramach okna"""
        key = pygame.key.get_pressed()

        if key[pygame.K_s]:
            if self.y>=screen_height-32:
                self.y=screen_height-32
            else:
                self.y += self.speed
        elif key[pygame.K_w]:
            if self.y<=0:
                self.y=0
            else:
                self.y -= self.speed
        if key[pygame.K_d]:
            if self.x>=screen_width-32:
                self.x=screen_width-32
            else:
                self.x += self.speed
        elif key[pygame.K_a]:
            if self.x<=0:
                self.x=0
            else:
                self.x -= self.speed

    def incrScore(self,amount):
        """zwieksza wartosc score (wynik)"""
        self.score+=amount

    def getScore(self):
        """zwraca wartosc score (wynik)"""
        return self.score

    def update(self,screen_width,screen_height):
        """aktualizuje obiekt gracza"""
        self.movement(screen_width,screen_height)
        self.levelUp()
        self.rect.x=self.x
        self.rect.y=self.y
        if self.hp == 0 or self.hp<0:
            self.kill()
