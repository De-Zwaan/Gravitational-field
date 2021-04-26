import pyopencl as cl
import numpy as np
import cv2

def compute(width, height, planets):
    # array with numbers as imput

    # in_shape = (len(planets), 1, 4)

    planet_x =          np.empty(len(planets)).astype(np.float32)
    planet_y =          np.empty_like(planet_x)
    planet_mass =       np.empty_like(planet_x)
    # image_in = np.zeros(in_shape, dtype=np.int32)

    # convert to 3 1d arrays
    for i in range(len(planets)):
        planet_x[i] =           planets[i].x
        planet_y[i] =           planets[i].y
        planet_mass[i] =        planets[i].m 
        # image_in[i][0] =        planets[i].c
    
    # Establish context
    platforms = cl.get_platforms() # a platform corresponds to a driver (e.g. AMD)
    platform = platforms[0] # take first platform
    devices = platform.get_devices(cl.device_type.GPU) # get GPU devices of selected platform
    device = devices[0] # take first GPU
    ctx = cl.Context([device]) # put selected GPU into context object
    queue = cl.CommandQueue(ctx, device) # create command queue for selected GPU and context

    # Get the shape from the input image
    image_in = cv2.imread('./grav_field.png', cv2.IMREAD_COLOR)

    out_shape = image_in.T.shape # (width, height, 4)
    image_out = np.empty_like(image_in) # np.zeros(out_shape, dtype=np.int32)

    in_shape = out_shape
    # Setup buffers
    mf = cl.mem_flags
    # planet_x_buf =      cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=planet_x)
    # planet_y_buf =      cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=planet_y)
    # planet_mass_buf =   cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=planet_mass)
    
    image_in_buf =      cl.Image(ctx, mf.READ_ONLY, cl.ImageFormat(cl.channel_order.LUMINANCE, cl.channel_type.UNORM_INT8), shape=in_shape) 
    image_out_buf =     cl.Image(ctx, mf.WRITE_ONLY, cl.ImageFormat(cl.channel_order.LUMINANCE, cl.channel_type.UNORM_INT8), shape=out_shape)
    
    # Build the program
    prg = cl.Program(ctx, open('./compute.cl').read()).build()

    # Run the program using the buffers
    kernel = cl.Kernel(prg, 'compute') 
    kernel.set_arg(0, image_in_buf) 
    # kernel.set_arg(1, planet_x_buf) 
    # kernel.set_arg(2, planet_y_buf)
    # kernel.set_arg(3, planet_mass_buf)
    kernel.set_arg(1, image_out_buf)

    cl.enqueue_copy(queue, image_in_buf, image_in, origin=(0, 0), region=in_shape).wait()
    cl.enqueue_nd_range_kernel(queue, kernel, out_shape, None, allow_empty_ndrange = True) 
    cl.enqueue_copy(queue, image_out, image_out_buf, origin=(0, 0), region=out_shape).wait()
    
    # Return the result
    return image_out