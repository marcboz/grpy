import pygame, playerobj

class Menu:
    def __init__(self):
        """obiekt menu"""

        self.menubg=pygame.image.load('images/menu.png')
        self.menubg.convert()

        self.pause=-1

        self.hpbtt=pygame.image.load('images/hpbut.png')
        self.hpbtt.convert()
        self.hprect=self.hpbtt.get_rect()

        self.shbtt=pygame.image.load('images/shieldbut.png')
        self.shbtt.convert()
        self.shrect=self.shbtt.get_rect()

        self.wpbtt=pygame.image.load('images/wpnbut.png')
        self.wpbtt.convert()
        self.wprect=self.wpbtt.get_rect()

        self.exbtt=pygame.image.load('images/exitbut.png')
        self.exbtt.convert()
        self.exrect=self.exbtt.get_rect()

        self.rebtt=pygame.image.load('images/backbut.png')
        self.rebtt.convert()
        self.rerect=self.rebtt.get_rect()

        self.stbtt=pygame.image.load('images/startbut.png')
        self.stbtt.convert()
        self.strect=self.stbtt.get_rect()

        self.oldtick=pygame.time.get_ticks()


    def getPause(self):
        """zraca wartosc pause (wartosc od ktorej zalezne jest ktore okno jest wyswietlane(startowe,gry,menu gry))"""
        return self.pause

    def setPause(self,to):
        """zmienia wartosc pause na wartosc argumentu to"""
        self.pause=to

    def menuUp(self,player):
        """funkcja odpowiadajaca za sprawdzanie ktory z przyciskow zostal klikniety (kup hp,kup tarcze,kup ulepszenie broni,wznow gre,wyjdz z gry)"""
        mouse=pygame.mouse.get_pressed()
        mpos=pygame.mouse.get_pos()

        if self.hprect.collidepoint(mpos) and mouse==(1,0,0) and player.getPlayerCash()>=250:
            currtick=pygame.time.get_ticks()
            if currtick-self.oldtick>500:
                player.refillHP()
                player.reduceCash(250)
                print("check")
                self.oldtick=currtick


        if self.shrect.collidepoint(mpos) and mouse==(1,0,0) and player.getPlayerCash()>=500:
            currtick=pygame.time.get_ticks()
            if currtick-self.oldtick>500:
                player.upgradeShield()
                player.reduceCash(500)
                print("check")
                self.oldtick=currtick

        if self.wprect.collidepoint(mpos) and mouse==(1,0,0) and player.getPlayerCash()>=500:
            currtick=pygame.time.get_ticks()
            if currtick-self.oldtick>500:
                player.upgradeWeapon()
                player.reduceCash(500)
                print("check")
                self.oldtick=currtick

        if self.rerect.collidepoint(mpos) and mouse==(1,0,0):
            currtick=pygame.time.get_ticks()
            if currtick-self.oldtick>500:
                self.setPause(0)
                self.oldtick=currtick

        if self.exrect.collidepoint(mpos) and mouse==(1,0,0):
            currtick=pygame.time.get_ticks()
            if currtick-self.oldtick>500:
                self.setPause(2)

        if self.strect.collidepoint(mpos) and mouse==(1,0,0):
            currtick=pygame.time.get_ticks()
            if currtick-self.oldtick>500:
                self.setPause(0)


    def menuUpdate(self,player,screen_width,screen_height,screen,casht,cash,background,font):
        """aktualizuje menu gry"""
        self.menuUp(player)

        txt1=font.render("500",1,(0,255,0))
        txt2=font.render("500",1,(0,255,0))
        txt3=font.render("250",1,(0,255,0))
        windowx=screen_width/2-200
        windowy=screen_height/2-125

        self.hprect.x=350
        self.hprect.y=175
        self.shrect.x=250
        self.shrect.y=175
        self.wprect.x=450
        self.wprect.y=175
        self.rerect.x=360
        self.rerect.y=285
        self.exrect.x=360
        self.exrect.y=325

        screen.blit(background,(0,0))
        screen.blit(self.menubg,(windowx,windowy))
        screen.blit(self.hpbtt,(self.hprect.x,self.hprect.y))
        screen.blit(self.shbtt,(self.shrect.x,self.shrect.y))
        screen.blit(self.wpbtt,(self.wprect.x,self.wprect.y))
        screen.blit(self.rebtt,(self.rerect.x,self.rerect.y))
        screen.blit(self.exbtt,(self.exrect.x,self.exrect.y))
        screen.blit(casht,(360,windowy+3))
        screen.blit(cash,(410,windowy+3))
        screen.blit(txt3,(387,255))
        screen.blit(txt2,(287,255))
        screen.blit(txt1,(487,255))

    def startMenu(self,screen_width,screen_height,screen,background,player,font):
        """aktualizuje menu startowe gry"""
        self.menuUp(player)

        txt=font.render("SPACE FIGHTER",1,(255,255,255))

        windowx=screen_width/2-200
        windowy=screen_height/2-125

        self.exrect.x=360
        self.exrect.y=290

        self.strect.x=350
        self.strect.y=250

        screen.blit(background,(0,0))
        screen.blit(txt,(0,20))
        screen.blit(self.stbtt,(self.strect.x,self.strect.y))
        screen.blit(self.exbtt,(self.exrect.x,self.exrect.y))
