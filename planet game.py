import pgzrun
import random

WIDTH = 800
HEIGHT = 600

TITLE = "click the planets in order"

address = []
planets=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune"]

for i in range(len(planets)):
    p = planets[i]+".png"
    print(p)
    mercury = Actor(p)
    mercury.x = random.randint(0,WIDTH)
    mercury.y = random.randint(0,HEIGHT)
    address.append(mercury)

def draw():
    screen.blit("space",(0,0))
    for i in address:
        i.draw()

pgzrun.go()
