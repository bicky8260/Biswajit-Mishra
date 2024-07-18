import os
import pygame
WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")
WHITE=(0,204,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

BULLET_VEL = 5
MAX_BULLETS = 10

BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
FPS = 60
spaceship_width,spaceship_height=55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
YELLOW_SPACESHIP=pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(spaceship_width,spaceship_height)),90)
RED_SPACESHIP=pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_spaceship=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(spaceship_width,spaceship_height)),270)
VEL = 5

def draw_window(yellow, red, red_bullets, yellow_bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(yellow_spaceship,(yellow.x,yellow.y))
    WIN.blit(red_spaceship,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)

    pygame.display.update()

def yellow_handle_movement(KEY_PRESSED,yellow):
    if KEY_PRESSED[pygame.K_a] and yellow.x - VEL > 0:
         yellow.x-=VEL
    if KEY_PRESSED[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
         yellow.x+=VEL
    if KEY_PRESSED[pygame.K_w] and yellow.y - VEL > 0:
         yellow.y-=VEL
    if KEY_PRESSED[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT-10:
         yellow.y+=VEL
def red_handle_movement(KEY_PRESSED,red):
    if KEY_PRESSED[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
         red.x-=VEL
    if KEY_PRESSED[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
         red.x+=VEL
    if KEY_PRESSED[pygame.K_UP] and red.y - VEL > 0:
         red.y-=VEL
    if KEY_PRESSED[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT-10:
        red.y+=VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
     for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

     for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
def main():
    yellow = pygame.Rect (100,300,spaceship_width,spaceship_height)
    red = pygame.Rect (700,300,spaceship_width,spaceship_height)
    
    red_bullets = []
    yellow_bullets = []
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
               run=False

          if  event.type==pygame.KEYDOWN:
              if event.key==pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                 bullet=pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height//2 - 2, 10, 5)
                 yellow_bullets.append(bullet)

              if event.key==pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                   bullet=pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                   red_bullets.append(bullet)
        

        print(red_bullets,yellow_bullets)
        KEY_PRESSED=pygame.key.get_pressed()
        yellow_handle_movement(KEY_PRESSED,yellow)
        red_handle_movement(KEY_PRESSED,red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(yellow, red, red_bullets, yellow_bullets)

    pygame.quit()

if __name__=="__main__":
    main()