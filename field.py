from PIL import Image, ImageDraw
import numpy as np
import math
import random as r
import cl as cl

class planet:
    def __init__(self, x, y, mass, color):
        self.x = x
        self.y = y
        self.m = mass
        self.c = color

def createImage():
    width = 1000
    height = 1000
    num_planets = 5


    img = Image.new('RGB', (width, height), color = 'black')
    draw = ImageDraw.Draw(img)

    planets = []
    for n in range(0, num_planets):
        planets.append(planet(r.randint(0, width), r.randint(0, height), r.random()*100, (r.randint(100, 255), r.randint(100, 255), r.randint(100, 255))))

    result = cl.compute(width, height, planets)

    for i in range(0, width):
        for j in range(0, height):
            color = planets[int(result[j * width + i])].c
            # print(color)
            # print(color)
            draw.point((i, j), fill = color)
    
    for p in planets:
        # draw.ellipse([(p.x - p.m / 10, p.y - p.m / 10), (p.x + p.m / 10, p.y + p.m / 10)], fill = (255, 100, 255))
        print()

    del draw
    img.save('./grav_field.png')

createImage()