import pgzrun
from pgzhelper import *
import random
import os 

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1000
HEIGHT = 700
TITLE = 'CAR_GAME'

street = Actor('street', (500, 350))
car1 = Actor('car1', (560, 80))
car2 = Actor('car2', (120, 400))
game_lost = Actor('game_lost', (500, 350))
repeat = Actor('repeat', (354, 499))

game_over = False

car1_speed = 4
car2_speed = 4
score = 0


def update():
    global car1_speed, car2_speed, score, game_over
    # print(score, car2_speed)
    
    # car1
    if keyboard.up and car1.y > 80 :
        car1.y -= car1_speed
    elif keyboard.down :
        car1.y += car1_speed
    if car1.y >= 800 :
        score += 1
        car1.y = -100
        if score == 5 :
            car2_speed += 2

    # car2
    car2.x += car2_speed
    if car2.x >= 1100 :
        car2.x = random.randint(-500, -100)
        # print(car2.x)

    # game_over
    if car1.colliderect(car2):
        game_over = True

    if game_over :
        car1_speed = 0
        car1_speed = 0
        score = 0
        car1.pos = 560, 80
        car2.pos = 120, 400





def draw():
    street.draw()
    car1.draw()
    car2.draw()
    screen.draw.text(
                    f'{score}',
                    fontsize= 60,
                    pos= (745, 105),
                    color= 'red',
                    background="gray",
                    shadow=(2,2), 
                    scolor="#202020"
                    )
    
    if game_over :
        game_lost.draw()
        repeat.draw()


def on_mouse_down(pos):
    global game_over, car1_speed, car2_speed

    if repeat.collidepoint(pos):
        game_over = False
        car1_speed = 4
        car2_speed = 4

    if car1.collidepoint(pos):
        print("on_mouse_down")
        sounds.horn1.play()
        # sounds.horn1.stop()


def on_key_down(key) :

    if key == keys.SPACE :
        print('on_key_down')
        sounds.horn2.play()


pgzrun.go()