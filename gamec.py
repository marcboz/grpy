import pygame,aliens,playerobj,projectiles,meteors,pickups

class Game:

    def checkGameOver(self,text,player,screen):
        if player.getPlayerHP()==0 or player.getPlayerHP()<0:
            screen.blit(text,(100,200))

    def update(self,player,alien_group,projectile_group,screen,background,screen_width,screen_height,playersprite,scoret,gameover,hpt,levelt,shieldt,casht,meteor_group,font1,font2,pickup_group):

        player.update()
        projectile_group.update(screen_width,alien_group,player)
        alien_group.update(projectile_group,player,screen_width,screen_height,pickup_group)
        meteor_group.update(player,screen_width,screen_height)
        pickup_group.update(player)

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
        self.checkGameOver(gameover,player,screen)
        playersprite.draw(screen)
        projectile_group.draw(screen)
        alien_group.draw(screen)
        meteor_group.draw(screen)
        pickup_group.draw(screen)
