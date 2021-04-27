__kernel void compute(const int f_mult, __global const float *planet_x, __global const float *planet_y, __global const float *planet_mass, __global const int *planet_color, __global uchar *res)
{
    // Don't question why x and why are not normal, it just works this way 
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
    int index = y * 3 * %d + x * 3 + z;

    float f_norm = max_planet_f * f_mult;
    if (f_norm < 0) {
        // Only possible if f_mult < 0 --> returns a flat image
        f_norm = 1;
    } else if (f_norm > 1) {
        // Upper threshold, higher is not recommended
        f_norm = 1;
    }

    // Return the planet with the highest influence on the current pixel
    res[index] = planet_color[max_planet_index * 3 + z] * f_norm;

}