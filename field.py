from PIL import Image, ImageColor, ImageDraw
import numpy as np
import math
import random as r
import cl as cl

class planet:
    def __init__(self, x, y, mass, radius, surf_color, color):
        self.x = x
        self.y = y
        self.m = mass
        self.surf_color = surf_color
        self.c = color
        self.r = radius

def getColor(h, s, v):
    # color = (r.randint(100, 255), r.randint(100, 255), r.randint(100, 255))
    # color = ImageColor.getrgb("hsl(" + str(r.randint(0, 360)) + ", " + str(50) +"%, " + str(75) + "%)")
    return ImageColor.getrgb("hsl(" + str(h) + ", " + str(s) +"%, " + str(v) + "%)")

def createImage():
    width = 1024
    height = 1024
    num_planets = r.randint(7, 15)


    img = Image.new('RGB', (width, height), color = 'black')
    draw = ImageDraw.Draw(img)

    planets = []
    i = r.randint(0, 360)
    for n in range(0, num_planets):
        # color = (r.randint(100, 255), r.randint(100, 255), r.randint(100, 255))
        color = getColor(r.randint(i*int(360 / num_planets), (i + 1)*int(360 / num_planets)), 75, 70)
        # color = ImageColor.getrgb("hsl(" + str(r.randint(0, 360)) + ", " + str(50) +"%, " + str(75) + "%)")
        planets.append(planet(r.randint(0, width), r.randint(0, height), r.random(), color))
        i = i + 1

    result = cl.compute(width, height, planets)

    Image.fromarray(result)
    
    # Add dots on the image for the locations of the planets
    for p in planets:
        draw.ellipse([(p.x - p.r, p.y - p.r), (p.x + p.r, p.y + p.r)], fill = p.surf_color)
    
    # for p in planets:
        # draw.ellipse([(p.x - p.m / 10, p.y - p.m / 10), (p.x + p.m / 10, p.y + p.m / 10)], fill = (255, 100, 255))
    del draw
    img.save('./grav_field.png')

createImage()