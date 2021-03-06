from PIL import Image, ImageColor
import numpy as np
import math
import random as r
import cl

class planet:
    def __init__(self, x, y, mass, radius, surface_color, field_color):
        self.x = x
        self.y = y
        self.m = mass
        self.r = radius
        self.surf_color = surface_color
        self.c = field_color

# A function to go from hsv to rgb, returns a tuple
def getColor(h, s, v):
    # color = (r.randint(100, 255), r.randint(100, 255), r.randint(100, 255))
    # color = ImageColor.getrgb("hsl(" + str(r.randint(0, 360)) + ", " + str(50) +"%, " + str(75) + "%)")
    return ImageColor.getrgb("hsl(" + str(h) + ", " + str(s) +"%, " + str(v) + "%)")

# Generate some nice looking planets
def generatePlanets(width, height, num_planets, c, planets):
    i = r.randint(0, 360)
    
    density = 1000
    r_scale = 2
    
    for n in range(0, num_planets):
        # Get a nice surface colour
        hue = r.randint(i*int(360 / num_planets), (i + 1)*int(360 / num_planets))
        i = i + 1

        surface_color =     c(hue, 75, 75)
        field_color =       c(hue, 70, 70)
        
        # Generate a mass and a radius
        mass = r.random()
        radius = (3 / (4 * math.pi) * mass * density)**(1/3) * r_scale
        
        # Add the new planet to the array
        planets.append(planet(r.randint(0, width), r.randint(0, height), mass, radius, surface_color, field_color))

    return planets

def createImage(width, height, planets):
    print("Started.")

    # Compute the color of every pixel
    result_BW =      cl.BWcompute(width, height, planets)
    result_Color =   cl.colorCompute(width, height, planets)

    result_color_weird = np.empty_like(result_BW)

    # Calculating the colors based on the brightness of the BW image
    print("Calculating...")
    # for i, x in np.ndenumerate(result_BW):
    #     result_color_weird[i[0]][i[1]] = getColor(x / 255 * 360, 70, 70)

    # Convert the resulting array into a picture
    print("Converting...")
    img_BW =    Image.fromarray(result_BW, 'RGB')
    img_Color = Image.fromarray(result_Color, 'RGB')

    img_weird = Image.blend(img_Color, img_BW, 0.5)
    img_color_weird = Image.fromarray(result_color_weird, 'RGB')

    # Save the image
    img_BW.save('./grav_field_BW.png')
    img_Color.save('./grav_field_color.png')
    img_weird.save('./grav_field_weird.png')
    img_color_weird.save('./grav_field_color_weird.png')
    print("Saved...")

# Dimensions of the final image
width = 2048
height = 2048

time = 1

# Empty array to store the planets
planets = []

# Randomly create some beautiful planets
# Comment out if you want to use your own planets
planets = generatePlanets(width, height, 8, getColor, planets)

# planets.append(planet(width/2, height/2, 1, 1, getColor(255, 255, 255), getColor(255, 255, 255)))

# Scales to display the different planets from out solar system at.
# Scale of the distance to the sun
d_scale = 128
# Scale of the planets themselves
r_scale = 1

# List of a few massive bodies from the solar system
# # sun
# planets.append(planet(width / 2, height,                332900 / 100, 109 * r_scale / 5,      getColor(50, 80, 70),   (0, 0, 0))) # getColor(50, 70, 80)))
# # mercury
# planets.append(planet(width / 2, height - 0.4 * d_scale,  0.055,      0.383 * r_scale,        getColor(205, 5, 50),   getColor(200, 10, 60)))
# # venus
# planets.append(planet(width / 2, height - 0.7 * d_scale,  0.815,      0.950 * r_scale,        getColor(0, 0, 60),     getColor(0, 0, 70)))
# # earth
# planets.append(planet(width / 2, height - 1.0 * d_scale,  1.000,      1.000 * r_scale,        getColor(205, 85, 60),  getColor(205, 80, 70)))
# # mars
# planets.append(planet(width / 2, height - 1.5 * d_scale,  0.107,      0.533 * r_scale,        getColor(20, 95, 70),   getColor(25, 90, 80)))
# # jupiter
# planets.append(planet(width / 2, height - 5.2 * d_scale,  318.0,      11.209 * r_scale,       getColor(25, 40, 55),   getColor(25, 40, 60)))
# # saturn
# planets.append(planet(width / 2, height - 9.5 * d_scale,  95.00,      9.449 * r_scale,        getColor(50, 55, 60),   getColor(55, 40, 70)))
# # uranus
# planets.append(planet(width / 2, height - 19.2 * d_scale, 14.00,      4.007 * r_scale,        getColor(180, 50, 75),  getColor(180, 45, 80)))
# # neptune
# planets.append(planet(width / 2, height - 30.1 * d_scale, 17.00,      3.883 * r_scale,        getColor(210, 80, 85),  getColor(210, 70, 75)))

# Create the image using the planets in the array
createImage(width, height, planets)
