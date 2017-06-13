import pygame, playerobj,aliens,projectiles,meteors,menuscr, sys,random
from pygame.locals import *

screen_width=800
screen_height=500

def checkGameOver(text,player,screen):
    if player.getPlayerHP()==0 or player.getPlayerHP()<0:
        screen.blit(text,(100,200))


def main():

    pygame.init()
    pygame.display.set_caption("gra")
    screen=pygame.display.set_mode([screen_width,screen_height])
    key = pygame.key.get_pressed()

    gamepaused=0

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
    pygame.time.set_timer(spawnalien,5000)

    spawnmeteor=pygame.USEREVENT+2
    pygame.time.set_timer(spawnmeteor,5000)

    alien_group=pygame.sprite.Group()
    meteor_group=pygame.sprite.Group()

    playersprite = pygame.sprite.RenderPlain((player))

    scoret=font1.render("SCORE:",1,(255,255,255))
    gameover=font2.render("GAME OVER",1,(255,255,255))
    hpt=font1.render("HP:",1,(255,0,0))
    levelt=font1.render("LVL:",1,(255,255,255))
    shieldt=font1.render("SHIELD:",1,(0,0,255))
    casht=font1.render("CASH:",1,(0,255,0))


    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.setPause(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    currtick=pygame.time.get_ticks()
                    if currtick-oldtick>800:
                        nprojectile=projectiles.Projectile(50,5,1,player.getxPosition(),player.getyPosition())
                        projectile_group.add(nprojectile)
                        oldtick=currtick
                        print("pew")
            if event.type == spawnalien:
                if menu.getPause() ==0:
                    alien=aliens.Alien(player,screen_width-35,random.randint(35,screen_height-35),random.randint(-5,0),random.randint(-5,5))
                    alien_group.add(alien)
            if event.type == spawnmeteor:
                if menu.getPause() ==0:
                    meteor=meteors.Meteor(1,screen_width-35,random.randint(35,screen_height-35),random.randint(-5,-1),random.randint(-5,5))
                    meteor_group.add(meteor)

        screen.blit(background,(0,0))

        if menu.getPause()==0:
            player.update()
            projectile_group.update(screen_width,alien_group,player)
            alien_group.update(projectile_group,player,screen_width,screen_height)
            meteor_group.update(player,screen_width,screen_height)

            score=font1.render(str(player.getScore()),1,(255,255,255))
            hp=font1.render(str(player.getPlayerHP()),1,(255,0,0))
            level=font1.render(str(player.getLevel()),1,(255,255,255))
            shield=font1.render(str(player.getPlayerShield()),1,(0,0,255))
            cash=font1.render(str(player.getPlayerCash()),1,(0,255,0))


            screen.blit(scoret,(screen_width-160,15))
            screen.blit(score,(screen_width-100,15))
            screen.blit(hpt,(50,15))
            screen.blit(hp,(80,15))
            screen.blit(levelt,(140,15))
            screen.blit(level,(170,15))
            screen.blit(shieldt,(210,15))
            screen.blit(shield,(280,15))
            screen.blit(casht,(320,15))
            screen.blit(cash,(370,15))
            checkGameOver(gameover,player,screen)
            playersprite.draw(screen)
            projectile_group.draw(screen)
            alien_group.draw(screen)
            meteor_group.draw(screen)

        if menu.getPause()==1:
            cash=font1.render(str(player.getPlayerCash()),1,(0,255,0))
            menu.menuUpdate(player,screen_width,screen_height,screen,casht,cash,background,font1)


        pygame.display.update()

        clock.tick(60)
        if menu.getPause()==2:
            pygame.quit()
            return

if __name__ == '__main__':main()
