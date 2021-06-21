# Gravitational-field

<b>Description:</b> A program to visualise the relative strength of gravitational fields. The result is surprisingly beautiful.<br>

Every pixel gets the color of the planet that has the strongest gravitational attraction on an object at that pixel. Based on Newtown's law of universal gravitation. <br>

<b>Languages / Dependencies:</b> Mostly written in Python 3.8.5, uses the numpy, PIL, random, math and pyopencl libraries. The kernel is written in OpenCL (C++)

<b>Possible results:</b><br>
<img src="https://user-images.githubusercontent.com/46651802/116305615-4d66f400-a7a4-11eb-9a80-e23faea332a4.png" width="480px">
<img src="https://user-images.githubusercontent.com/46651802/116306291-2bba3c80-a7a5-11eb-840f-12301977773f.png" width="480px">

# How to run #
Clone the repo and edit the settings in field.py until the desired effect is achieved. Run the script, a file called grav_field.png will appear in the folder.
