from vpython import *

canvas(background=color.cyan)
'''s1=sphere(radius=3)
s2=
shape.color=color.red'''
def knight(pos):
    # Create the base cylinder
    k1=cylinder(pos=vector(0,0,0), axis=vector(0, 1, 0), radius=0.6,length=3)
    # Create the top sphere
    k5=sphere(pos=pos+vector(0, 3, 0), radius=0.6)
    # Create the head of the horse
    k2=box(pos=pos+vector(0, 0, 0),size=vector(1.2,0.5,1.2))
    # Create the ears of the horse
    k3=cylinder(pos=pos+vector(0.25, 4, 0), axis=vector(0, -1, 0), radius=0.05)
    k4=cylinder(pos=pos+vector(-0.25,4, 0), axis=vector(0, -1, 0), radius=0.05)

    k=compound([k1,k2,k3,k4,k5])
    k.shininess=0.2
    k.emissive=False
    k.texture='download.jpg'

knight(vector(0, 0, 0))
while True:pass