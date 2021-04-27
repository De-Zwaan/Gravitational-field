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

def generatePlanets(width, height, num_planets, c):
    # Initialise the planets in an array
    planets = []
    i = r.randint(0, 360)

    for n in range(0, num_planets):
        # Get a nice colour
        hue = r.randint(i*int(360 / num_planets), (i + 1)*int(360 / num_planets))
        i = i + 1
        color = c(hue, 70, 70)

        # Add the new planet to the array
        planets.append(planet(r.randint(0, width), r.randint(0, height), r.random(), color))

    return planets

def createImage(width, height, planets):
    img = Image.new('RGB', (width, height), color = 'black')

    # Compute the color of every pixel
    result = cl.compute(width, height, planets)

    # Convert the resulting array into a picture
    img = Image.fromarray(result, 'RGB')
    draw = ImageDraw.Draw(img)
    
    # Add dots on the image for the locations of the planets
    for p in planets:
        draw.ellipse([(p.x - p.r, p.y - p.r), (p.x + p.r, p.y + p.r)], fill = p.surf_color)
    
    del draw

    # Save the image
    img.save('./grav_field.png')

createImage()