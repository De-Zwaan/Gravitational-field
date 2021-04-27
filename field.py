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

# Generate some nice looking planets
def generatePlanets(width, height, num_planets, c, planets):
    i = r.randint(0, 180)
    
    density = 1000
    r_scale = 2
    
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
    # for p in planets:
    #     draw.ellipse([(p.x - p.r, p.y - p.r), (p.x + p.r, p.y + p.r)], fill = p.surf_color)
    
    del draw

    # Save the image
    img.save('./grav_field.png')

# Dimensions of the final image
width =     1024
height =    1024

scale = 128
r_scale = 1

time = 1

planets = []

# Randomly create some beautiful planets
# Comment out if you want to use your own planets
# planets = generatePlanets(width, height, 7, getColor, planets)

# ------------------ CUSTOM PLANETS ----------------------------------
# Scales to display the different planets from out solar system at.
# Scale of the distance to the sun
d_scale = 150
# Scale of the planets themselves
r_scale = 1

# sun
planets.append(planet(width / 2, height / 2,                332900,     109 * r_scale / 5,          getColor(50, 80, 70),   (0, 0, 0)))
# mercury
planets.append(planet(width / 2, height / 2 - 0.4 * d_scale,  0.055,      0.383 * r_scale,        getColor(205, 5, 65),   getColor(200, 10, 60)))
# venus
planets.append(planet(width / 2, height / 2 - 0.7 * d_scale,  0.815,      0.950 * r_scale,        getColor(0, 0, 80),     getColor(0, 0, 70)))
# earth
planets.append(planet(width / 2, height / 2 - 1.0 * d_scale,  1.000,      1.000 * r_scale,        getColor(205, 85, 80),  getColor(205, 80, 70)))
# mars
planets.append(planet(width / 2, height / 2 - 1.5 * d_scale,  0.107,      0.533 * r_scale,        getColor(20, 95, 90),   getColor(25, 90, 80)))
# jupiter
planets.append(planet(width / 2, height / 2 - 5.2 * d_scale,  318.0,      11.209 * r_scale,       getColor(25, 40, 75),   getColor(25, 40, 60)))
# saturn
planets.append(planet(width / 2, height / 2 - 9.5 * d_scale,  95.00,      9.449 * r_scale,        getColor(50, 55, 80),   getColor(55, 40, 70)))
# uranus
planets.append(planet(width / 2, height / 2 - 19.2 * d_scale, 14.00,      4.007 * r_scale,        getColor(180, 50, 95),  getColor(180, 45, 80)))
# neptune
planets.append(planet(width / 2, height / 2 - 30.1 * d_scale, 17.00,      3.883 * r_scale,        getColor(210, 80, 85),  getColor(210, 70, 75)))

createImage(width, height, planets)