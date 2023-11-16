import pygame
import time
import random

pygame.font.init()

pygame.mixer.init()

WIDTH, HEIGHT = 800, 500
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Dodge')

BG = pygame.transform.scale(pygame.image.load('/Programming/Python/Mini Projects/bg image.jpg'),(WIDTH, HEIGHT))

pygame.mixer.music.load('/Programming/Python/Mini Projects/bg music 1.mp3')
pygame.mixer.music.play()

PLAYER_WIDTH = 40
PLAYER_HEIGHT= 60

PLAYER_VEL = 5

STAR_WIDTH = 5
STAR_HEIGHT = 10

STAR_VEL = 1

FONT = pygame.font.SysFont('comicsans',30)
FONT_LOST = pygame.font.SysFont('comicsans',100)

def draw(player,elapsed_time,stars):
    WIN.blit(BG,(0,0))

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1 ,'White' )
    WIN.blit(time_text,(10,10))

    pygame.draw.rect(WIN,'Red',player)

    for star in stars:
        pygame.draw.rect(WIN, 'Orange', star)

    pygame.display.update()

def main():
    run = True

    player  = pygame.Rect(200,HEIGHT-PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    stars = []

    hit = False 

    while run:

        star_count += clock.tick(100)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(2):
                star_x = random.randint(0,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <=  WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + STAR_HEIGHT >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            pygame.mixer.music.stop()
        
        if hit:
            lost_text = FONT_LOST.render('YOU LOST !', 1, 'Green')
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player,elapsed_time,stars)
        
    pygame.quit()

if __name__ == '__main__':
    main()