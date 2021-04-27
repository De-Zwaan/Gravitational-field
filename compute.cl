__kernel void compute(const int width, const int height, __global const float *planet_x, __global const float *planet_y, __global const float *planet_mass, __global const int *planet_color, __global uchar *res)
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