from vpython import *

#Create a 3D scene
scene = canvas(width=1280, height=720)

#Create a 3D model of the earth
earth = sphere(pos = vector(0,0,0), radius=1, texture=textures.earth)

#Run Animation
while True:
    rate(60) #Frame rate

def change_radius(evt):
        rad = evt.number
        if rad != None:
                if rad < 10:
                        ss.radius=evt.number
                else:
                        print(rad + ' is too large')
                        ww.text = ''

scene.append_to_caption('Radius must be less than 10 \n')
ww = winput(prompt='Radius:', bind=change_radius, type='numeric')