from vpython import *

def pawn(pos):
    p1=cylinder(radius=0.5,length=0.25,pos=pos,axis=vector(0,-1,0))
    p2=box(width=0.5,height=0.5,length=1.3,pos=pos+vector(0,0.6,0),axis=vector(0,-1,0))
    p3=sphere(radius=0.27,pos=pos+vector(0,1.3,0))
    p4=cylinder(radius=0.4,length=0.15,pos=pos+vector(0,1.3,0),axis=vector(0,-1,0))
    pawn=compound([p1,p2,p3,p4])
    pawn.texture='stone.jpg'
    pawn.shininess=0.0