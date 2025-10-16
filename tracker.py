from vpython import *

# Create a 3D scene with Jupyter notebook mode disabled
# This allows VPython to work in cloud environments like Replit
scene = canvas(width=1280, height=720)
scene.caption = "3D Earth Satellite Tracker"

# Create a 3D model of the earth
earth = sphere(pos=vector(0,0,0), radius=1, texture=textures.earth)

# Run Animation
while True:
    rate(60)  # Frame rate (60 FPS)
    earth.rotate(angle=0.01, axis=vector(0,1,0))  # Slow rotation
