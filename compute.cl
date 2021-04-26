constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_FILTER_NEAREST | CLK_ADDRESS_CLAMP_TO_EDGE;

__kernel void compute(__read_only image2d_t image_in, /*__global const float *planet_x, __global const float *planet_y, __global const float *planet_mass*/ __write_only image2d_t image_out)
{
    const int x = get_global_id(0);
    const int y = get_global_id(1);
    

    // // Set the start values for the comparison
    // int max_planet_index = -1;
    // float max_planet_f = 0;

    // // Loop over all the planets and calculate all the forces on the current pixel
    // for (int n = 0; n < sizeof(planet_mass); n++) {
    //     float f = planet_mass[n] / (pow(planet_x[n] - x, 2) + pow(planet_y[n] - y, 2));

    //     // Get the highest force
    //     if (f > max_planet_f) {
    //         max_planet_f = f;
    //         max_planet_index = n;
    //     }    
    // }

    // Return the planet with the highest influence on the current pixel
    int4 pixel_color = read_imagei(image_in, sampler, (int2)(x, y));
    printf("%s", pixel_color.s0);
    write_imagei(image_out, (int2)(x, y), (int4)(pixel_color));
}