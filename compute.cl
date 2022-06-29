__kernel void BWcompute(const int width, const int height, __global const float *planet_x, __global const float *planet_y, __global const float *planet_mass, __global uchar *res)
{
    // const int i = get_global_id(0);
    
    const int y = get_global_id(0);
    const int x = get_global_id(1);
    const int z = get_global_id(2);

    // Set empty vector
    float vec[2] = {0, 0};

    // Loop over all the planets and calculate all the forces on the current pixel
    for (int n = 0; n <= sizeof(planet_mass); n++) {
        // Calculate the distance
        float d2 = pown((planet_x[n] - x), 2) + pown((planet_y[n] - y), 2);
        
        // Avoid div0
        if (planet_x[n] == x && planet_y[n] == y) {break;}

        // Calculate the vector pointing towards each planet scaled by the mass of that planet
        float point[2] = {(planet_x[n] - x)*planet_mass[n]/d2, (planet_y[n] - y)*planet_mass[n]/d2};

        // Add the vector to the point
        vec[0] += point[0];
        vec[1] += point[1];
    }
    
    // Initialise empty direction float
    float dir = 0;

    // If the vector is 0, return a direction of 0
    if (vec[0] == 0 && vec[1] == 0) { 
        dir = 0;

    // If the vector points up, then the angle must be between 0 and pi
    } else if (vec[1] >= 0) {
        // Return the direction of the vector
        dir = acos(vec[0] / sqrt(pown(vec[0], 2) + pown(vec[1], 2)));

    // If the vector points down, then the angle must be between pi and 2pi
    } else if (vec[1] < 0) {
        dir = (2 * M_PI) - acos(vec[0] / sqrt(pown(vec[0], 2) + pown(vec[1], 2)));
    }

    // Convert x, y, z to an index
    int index = y * 3 * width + x * 3;

    // Return the direction as an angle between 0 and 1
    res[index + z] = (unsigned char)(dir / (2 * M_PI) * 255);
}

__kernel void colorCompute(const int width, const int height, __global const float *planet_x, __global const float *planet_y, __global const float *planet_mass, __global const int *planet_color, __global uchar *res)
{
    // const int i = get_global_id(0);
    
    const int y = get_global_id(0);
    const int x = get_global_id(1);
    const int z = get_global_id(2);

    // Set the start values for the comparison
    int max_planet_index = -1;
    float max_planet_f = 0;

    // Loop over all the planets and calculate all the forces on the current pixel
    for (int n = 0; n <= sizeof(planet_mass); n++) {
        // Avoid div0
        if (planet_x[n] == x && planet_y[n] == y) { max_planet_index = n; break; }
        
        // Calculate the force
        float f = planet_mass[n] / (pow(planet_x[n] - x, 2) + pow(planet_y[n] - y, 2));

        // Get the highest force
        if (f > max_planet_f) {
            max_planet_f = f;
            max_planet_index = n;
        }    
    }

    // Convert x, y, z to an index
    int index = y * 3 * width + x * 3 + z;

    if (max_planet_index == -1) {
        res[index] = 0;
    }

    // Return the planet with the highest influence on the current pixel
    res[index] = planet_color[max_planet_index * 3 + z];
}