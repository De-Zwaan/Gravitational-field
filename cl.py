import pyopencl as cl
import numpy as np

def compute(width, height, planets):
    # array with numbers as imput
    planet_x =          np.empty(len(planets)).astype(np.float32)
    planet_y =          np.empty_like(planet_x)
    planet_mass =       np.empty_like(planet_x)

    # convert to 3 1d arrays
    for i in range(len(planets)):
        planet_x[i] =       planets[i].x
        planet_y[i] =       planets[i].y
        planet_mass[i] =    planets[i].m 
    
    # array like a as output
    res = np.zeros((width * height)).astype(np.int32)
    
    print(res)

    # Establish context
    plat = cl.get_platforms()
    devices = plat[0].get_devices()
    ctx = cl.Context([devices[0]])
    ctx.get_info(cl.context_info.DEVICES)

    # Create a queue
    queue = cl.CommandQueue(ctx)

    # Setup buffers
    mf = cl.mem_flags
    planet_x_buf =      cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=planet_x)
    planet_y_buf =      cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=planet_y)
    planet_mass_buf =   cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=planet_mass)
    
    dest_buf = cl.Buffer(ctx, mf.WRITE_ONLY, res.nbytes)

    # Build the program
    f = open('./compute.cl', 'r')
    prg = cl.Program(ctx, "".join(f.readlines())).build()

    # Run the program using the buffers
    prg.compute(queue, res.shape, None, np.int32(width), np.int32(height), planet_x_buf, planet_y_buf, planet_mass_buf, dest_buf)

    # Get the result
    cl.enqueue_copy(queue, res, dest_buf)

    # Print the result
    print(res)
    return res