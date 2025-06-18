import pygame
pygame.init()
car_x=100
car_y=100
car_width=40
car_height=20
car_color=(0,0,255)
car_speed=5

screen=pygame.display.set_mode((480,360))
pygame.display.set_caption("Car Maze Game")
clock=pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x-=car_speed
    if keys[pygame.K_RIGHT]:
        car_x+=car_speed
    if keys[pygame.K_UP]:
        car_y-=car_speed
    if keys[pygame.K_DOWN]:
        car_y+=car_speed
    screen.fill((0,255,0))
    pygame.draw.circle(screen, car_color, (car_x, car_y), 10)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
 
