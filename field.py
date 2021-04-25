from PIL import Image, ImageDraw
import numpy as np
import math
import random as r

class planet:
    def __init__(self, x, y, mass, color):
        self.x = x
        self.y = y
        self.m = mass
        self.c = color

def calculateColour(planets, x, y, m):
    l = []
    for obj in planets:
        if obj.x != x or obj.y != y: 
            F = obj.m / math.sqrt((obj.x - x)**2 + (obj.y - y)**2 )
            l.append([F, obj])
        else:
            return (0, 0, 0)

    max = returnHighest(l)
    # print(max)
    return max[1].c

def returnHighest(arr):
    max = [0, 'null']
    # print(arr)
    for o in arr: 
        if o[0] > max[0]:
            max = o

    return max

def createImage():
    width = 1000
    height = 1000

    img = Image.new('RGB', (width, height), color = 'black')
    draw = ImageDraw.Draw(img)

    planets = []
    for n in range(0, 5):
        planets.append(planet(r.randint(0, width), r.randint(0, height), r.random()*100, (r.randint(100, 255), r.randint(100, 255), r.randint(100, 255))))

    for i in range(0, width):
        for j in range(0, height):
            color = calculateColour(planets, i, j, 1)
            # print(color)
            draw.point((i, j), fill = color)
    
    for p in planets:
        draw.ellipse([(p.x - p.m / 10, p.y - p.m / 10), (p.x + p.m / 10, p.y + p.m / 10)], fill = (255, 100, 255))
    
    del draw
    img.save('./grav_field.png')

createImage()