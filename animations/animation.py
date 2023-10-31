import pgzrun
from pgzhelper import *
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 1200
HEIGHT = 1000

pig = Actor("pig1" , (600,500))
pig.images = ["pig2" , "pig3" , "pig4" , "pig5" , "pig6" , "pig7" , "pig8" , "pig9" , "pig10" , "pig11" , "pig12"]
pig.fps = 10

pig_idle = Actor("pig1" , (600,500))
pig_idle.images = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"]
pig_idle.fps = 25

pig_jump = Actor("pig1" , (600,500))
pig_jump.images = ["j1","j2","j3","j4","j5","j6","j7","j8","j9","j10","j11","j12"]
pig_jump.fps = 15

def update():
    if keyboard.right:
        pig.animate()
        pig.flip_x = False
        
    elif keyboard.left:
        pig.animate()
        pig.flip_x = True
    elif keyboard.up:
        pig_jump.animate()
        pig.x += 5
        pig.x -= 5
        pig.image = pig_jump.image     
    else:
        if pig.flip_x == True:
            pig.flip_x = True
            pig_idle.animate()
            pig.image = pig_idle.image     
        else:
            pig.flip_x = False
            
            pig_idle.animate()
            pig.image = pig_idle.image  


        
def draw():
    screen.fill("white")
    pig.draw()
    
pgzrun.go()                