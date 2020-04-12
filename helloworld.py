import pygame
from pygame.locals import *
import sys

pygame.init()

FPS = 30
fps_clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((800, 500))
pygame.display.set_caption('House')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
maroon = (128, 0, 0)
olive = (128, 128, 0)
aqua = (0, 255, 255)

# spoopy shadow
shadow_img = pygame.image.load('spoopy_guy.png')
shadowx = 600
shadowy = 275
# direction = 'right'

smoke_ellipse_x = 85
smoke_ellipse_y = 120

# Main Game Loop
elapsed_time = 0
while True:
    # Draw on the surface object
    display_surface.fill(black)
    # House
    polygon_points = ((250, 200), (385, 285), (385, 470), (115, 470), (115, 285))
    pygame.draw.polygon(display_surface, white, polygon_points)
    # Porthole Window
    pygame.draw.line(display_surface, maroon, (250, 332), (250, 268), 3)
    pygame.draw.line(display_surface, maroon, (215, 300), (285, 300), 3)
    pygame.draw.circle(display_surface, olive, (250, 300), 35, 3)
    # Door
    pygame.draw.rect(display_surface, aqua, (215, 365, 70, 100))
    pygame.draw.rect(display_surface, maroon, (215, 365, 70, 100), 3)
    pygame.draw.line(display_surface, maroon, (215, 365), (285, 465), 3)
    pygame.draw.line(display_surface, maroon, (215, 465), (285, 365), 3)
    pygame.draw.circle(display_surface, maroon, (230, 420), 7)
    # Chimney
    pygame.draw.rect(display_surface, white, (170, 300, 25, 75))
    # Stars
    pixel_obj = pygame.PixelArray(display_surface)
    pixel_obj[425][425] = white
    pixel_obj[455][350] = white
    pixel_obj[325][200] = white
    pixel_obj[355][150] = white
    pixel_obj[427][175] = white
    pixel_obj[100][200] = white
    pixel_obj[50][300] = white
    pixel_obj[75][325] = white
    pixel_obj[65][400] = white
    del pixel_obj

    # Title
    # D
    pygame.draw.line(display_surface, white, (500, 55), (505, 105), 2)
    pygame.draw.line(display_surface, white, (500, 55), (523, 68), 2)
    pygame.draw.line(display_surface, white, (523, 68), (505, 105), 2)
    # O
    pygame.draw.line(display_surface, white, (535, 68), (540, 85), 2)
    pygame.draw.line(display_surface, white, (535, 68), (545, 55), 2)
    pygame.draw.line(display_surface, white, (545, 55), (565, 70), 2)
    pygame.draw.line(display_surface, white, (565, 70), (555, 85), 2)
    pygame.draw.line(display_surface, white, (555, 85), (540, 85), 2)
    # N
    pygame.draw.line(display_surface, white, (585, 55), (585, 102), 2)
    pygame.draw.line(display_surface, white, (585, 55), (598, 102), 2)
    pygame.draw.line(display_surface, white, (598, 55), (598, 102), 2)
    # T
    pygame.draw.line(display_surface, white, (615, 50), (645, 51), 2)
    pygame.draw.line(display_surface, white, (630, 50), (629, 102), 2)
    # L
    pygame.draw.line(display_surface, white, (550, 150), (549, 200), 2)
    pygame.draw.line(display_surface, white, (549, 200), (575, 198), 2)
    # O
    pygame.draw.line(display_surface, white, (570, 150), (575, 175), 2)
    pygame.draw.line(display_surface, white, (575, 175), (595, 180), 2)
    pygame.draw.line(display_surface, white, (595, 180), (605, 165), 2)
    pygame.draw.line(display_surface, white, (605, 165), (595, 140), 2)
    pygame.draw.line(display_surface, white, (595, 140), (570, 150), 2)
    # O
    pygame.draw.line(display_surface, white, (625, 168), (630, 185), 2)
    pygame.draw.line(display_surface, white, (625, 168), (635, 155), 2)
    pygame.draw.line(display_surface, white, (635, 155), (655, 170), 2)
    pygame.draw.line(display_surface, white, (655, 170), (645, 185), 2)
    pygame.draw.line(display_surface, white, (645, 185), (630, 185), 2)
    # K
    pygame.draw.line(display_surface, white, (675, 150), (674, 200), 2)
    pygame.draw.line(display_surface, white, (675, 175), (695, 148), 2)
    pygame.draw.line(display_surface, white, (675, 175), (693, 205), 2)


    if elapsed_time > 5000:
        display_surface.blit(shadow_img, (shadowx, shadowy))
        if elapsed_time > 5250:
            elapsed_time = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.ellipse(display_surface, white, (smoke_ellipse_x, smoke_ellipse_y, 100, 50))
    if smoke_ellipse_x == 85:
        smoke_ellipse_x -= 5
    elif smoke_ellipse_x == 0:
        smoke_ellipse_x = 85
    pygame.draw.circle(display_surface, white, (170, 168), 18)

    pygame.display.update()
    elapsed_time += fps_clock.tick(FPS)
