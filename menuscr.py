import pygame, playerobj

class Menu:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.menubg=pygame.image.load('images/menu.png')
        self.menubg.convert()

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

        self.oldtick=pygame.time.get_ticks()

    def menuUp(self,player,pause):
        mouse=pygame.mouse.get_pressed()
        mpos=pygame.mouse.get_pos()

        if hprect.collidepoint(mpos) and mouse==(1,0,0) and player.getPlayerCash>500:
            player.refillHP()

        if shrect.collidepoint(mpos) and mouse==(1,0,0) and player.getPlayerCash>1000:
            player.upgradeShield()

        if wprect.collidepoint(mpos) and mouse==(1,0,0) and player.getPlayerCash>1000:
            player.upgradeWeapon()

        if rerect.collidepoint(mpos) and mouse==(1,0,0):
            pause=0

        if exrect.collidepoint(mpos) and mouse==(1,0,0):
            pygame.quit()
            return
