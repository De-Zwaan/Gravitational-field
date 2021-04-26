import numpy as np
import math
import random as r
import cl
import cv2

class planet:
    def __init__(self, x, y, mass, color):
        self.x = x
        self.y = y
        self.m = mass
        self.c = color

def createImage():
    width = 255
    height = 255
    num_planets = 1

    planets = []
    for n in range(0, num_planets):
        planets.append(planet(r.randint(0, width), r.randint(0, height), r.random()*100, (r.randint(100, 255), r.randint(100, 255), r.randint(100, 255), 255)))

    print('starting computation')
    result = cl.compute(width, height, planets)
    cv2.imwrite('./grav_field.png', result) # , cv2.COLOR_RGBA2RGB)

createImage()