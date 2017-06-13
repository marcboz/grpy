import pygame, playerobj,aliens,projectiles,meteors,menuscr,gamec,pickups, sys,random
from pygame.locals import *

screen_width=800
screen_height=500

def main():

    pygame.init()
    pygame.display.set_caption("gra")
    screen=pygame.display.set_mode([screen_width,screen_height])
    key = pygame.key.get_pressed()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((15,15,15))

    font1=pygame.font.Font("fonts/arial.ttf",15)
    font2=pygame.font.Font("fonts/arial.ttf",100)

    screen.blit(background,(0,0))
    clock=pygame.time.Clock()
    oldtick=pygame.time.get_ticks()

    menu=menuscr.Menu()

    player=playerobj.Player(200,200,4)
    projectile_group=pygame.sprite.Group()

    spawnalien=pygame.USEREVENT+1
    spawnmeteor=pygame.USEREVENT+2


    alien_group=pygame.sprite.Group()
    meteor_group=pygame.sprite.Group()
    pickup_group=pygame.sprite.Group()

    playersprite = pygame.sprite.RenderPlain((player))

    scoret=font1.render("SCORE:",1,(255,255,255))
    gameover=font2.render("GAME OVER",1,(255,255,255))
    hpt=font1.render("HP:",1,(255,0,0))
    levelt=font1.render("LVL:",1,(255,255,255))
    shieldt=font1.render("SHIELD:",1,(0,0,255))
    casht=font1.render("CASH:",1,(0,255,0))

    game=gamec.Game()

    oldlvl=0

    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if menu.getPause()==-1:
                        menu.setPause(2)
                    if menu.getPause()==0:
                        menu.setPause(1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    currtick=pygame.time.get_ticks()
                    if currtick-oldtick>800:
                        nprojectile=projectiles.Projectile(player.getPlayerPower(),5,1,player.getxPosition(),player.getyPosition())
                        projectile_group.add(nprojectile)
                        oldtick=currtick

            if event.type == spawnalien:
                if menu.getPause() ==0:
                    alien=aliens.Alien(player,screen_width-35,random.randint(35,screen_height-35),random.randint(-5,-1),random.randint(-5,5))
                    alien_group.add(alien)
            if event.type == spawnmeteor:
                if menu.getPause() ==0:
                    meteor=meteors.Meteor(screen_width-35,random.randint(35,screen_height-35),random.randint(-5,-1),random.randint(-5,5),player)
                    meteor_group.add(meteor)

        if oldlvl<player.getLevel() and 5000-(200*player.getLevel())>=1000:
            pygame.time.set_timer(spawnalien,5000-(150*player.getLevel()))
            pygame.time.set_timer(spawnmeteor,5100-(150*player.getLevel()))
            oldlvl=player.getLevel()

        screen.blit(background,(0,0))

        if menu.getPause()==-1:
            menu.startMenu(screen_width,screen_height,screen,background,player,font2)

        if menu.getPause()==0:
            game.update(player,alien_group,projectile_group,screen,background,screen_width,screen_height,playersprite,scoret,gameover,hpt,levelt,shieldt,casht,meteor_group,font1,font2,pickup_group)

        if menu.getPause()==1:
            cash=font1.render(str(player.getPlayerCash()),1,(0,255,0))
            menu.menuUpdate(player,screen_width,screen_height,screen,casht,cash,background,font1)


        pygame.display.update()

        clock.tick(60)
        if menu.getPause()==2:
            pygame.quit()
            return

if __name__ == '__main__':main()
