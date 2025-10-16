from vpython import *

#Create a 3D scene
scene = canvas(width=1280, height=720)

#Create a 3D model of the earth
earth = sphere(pos = vector(0,0,0), radius=1, texture=textures.earth)

#Run Animation
while True:
    rate(60) #Frame rate
