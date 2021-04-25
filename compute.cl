__kernel void compute(const int width, const int height, __global const float *planet_x, __global const float *planet_y, __global const float *planet_mass, __global int *c)
{
    int i = get_global_id(0);
    
    // Set the start values for the comparison
    int max_planet_index = -1;
    float max_planet_f = 0;

    // Loop over all the planets and calculate all the forces on the current pixel
    for (int n = 0; n < sizeof(planet_mass); n++) {
        float f = planet_mass[n] / (pow(planet_x[n] - (i % width), 2) + pow(planet_y[n] - (i / width), 2));

        // Get the highest force
        if (f > max_planet_f) {
            max_planet_f = f;
            max_planet_index = n;
        }    
    }

    // Return the planet with the highest influence on the current pixel
    c[i] = max_planet_index;
}

/*
def calculateColour(planets, x, y, m):
    l = []
    for obj in planets:
        if obj.x != x or obj.y != y: 
            F = obj.m / ((obj.x - x)**2 + (obj.y - y)**2)
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
*/