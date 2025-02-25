import pygame, sys, os
import random

width = 400
height = 600
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
g = 0.5  
score = 0
fps = 13
fruits = ['watermelon', 'orange']

pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(white)
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 32)
score_text = font.render(str(score), True, black, white)

def generate_random_fruits(fruit):
    path = os.path.join(os.getcwd(), fruit+'.png')
    data[fruit] = {
        'img' : pygame.image.load(path),
        'x' : random.randint(50, 350),  
        'y' : 600,
        'speed_x' : random.randint(-5, 5),  
        'speed_y' : random.randint(-40, -30),  
        'throw' : False,
        't' : 0,
        'hit' : False,
    }

    if(random.random() >= 0.75):
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

pygame.display.update()

frame_counter = 0 

while True:
    gameDisplay.fill(white)
    gameDisplay.blit(score_text, (0,0))
    for key, value in data.items():
        if value['throw']:
            value['x'] = value['x'] + value['speed_x']
            value['y'] = value['y'] + value['speed_y']
            value['speed_y'] += (g * value['t'])
            value['t'] += 1

            if value['y'] <= height:
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                value['throw'] = False

            current_position = pygame.mouse.get_pos()
            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x'] + 60 and current_position[1] > value['y'] and current_position[1] < value['y'] + 60:
                path = os.path.join(os.getcwd(), 'half_' + key + '.png')
                value['img'] = pygame.image.load(path)
                value['speed_x'] += 10
                score += 1
                score_text = font.render(str(score), True, black, white)
                value['hit'] = True
        else:
            value['t'] = 0 

    frame_counter += 1 
    if frame_counter % (fps * 2) == 0:  
        for fruit in fruits:
            if not data[fruit]['throw']:
                generate_random_fruits(fruit)

    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
