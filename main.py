import pygame, sys
import math
from sprite import Sprite
from sprite_controlled import SpriteControlled
def main():

    #Load
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    font = pygame.font.Font(None,24)
    pygame.mouse.set_visible(False)
    player = SpriteControlled(100,400,'player.png', 2)
    quit = False

    #Text
    col_text = font.render("Im walking over here!", False,(0,0,0))

    #Paths
    path = 'D:\\AdventureGame\\'
    background = pygame.image.load(path+'background.png').convert()
    ground = pygame.image.load(path+'ground.png').convert()
    #player = Sprite(100,400,"player.png")
    friend = Sprite(500,400, "friend.png", 2)
    cursor = pygame.image.load(path+'mouse.png').convert_alpha()

    while not(quit):
        #Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = pygame.mouse.get_pos()
                player.move_to(cursor_pos[0])
        
        #Update
        
        player.update()

        cursor_pos = pygame.mouse.get_pos()     

        #Draw 
        screen.fill((0,0,0)) #screen color, 0,0,0 is black
        screen.blit(background, (0,0))
        screen.blit(ground,(0,424))
        player.draw(screen)
        friend.draw(screen)
        if(player.intersects(friend)):
            screen.blit(col_text,(player.x,player.y - 100))
        screen.blit(cursor,cursor_pos)
        pygame.display.update() #changes screen to new updated one

if __name__ == "__main__":
    main()