from vpython import *
import heapq
from time import *
import numpy as np
from ShortestPath import *
from Random_Obstacle import generate_obstacle_coordinates
from pawn import *

canvas(background=vector(0.1,0.2,0.2),title='THE LAST KNIGHT STANDING')
T = text(text='THE LAST KNIGHT STANDING', align='center', pos=vector(0,10,0), color=color.white)
n=''

def chess(n):
    global size
    n=int(n.text)
    size=n
    n=n//2
    for i in range(-n,n):
        for j in range(-n,n):
            rate(75)
            if (i+j) % 2 == 1 or (i+j) % 2 == -1:
                sColor = color.blue
            else: sColor = color.white
            box(pos=vector(i,0.1,j),length=1,height=0.1,width=1,color=sColor,texture='download.jpg')
    

#------------------Input to be taken here-------------------------------

size=0
src=''
dst=''
lst=[]
Route=[]


def s(s):
    global src
    global dst
    global lst
    global size
    global Route
    s=(s.text).split(',')
    s=[int(x) for x in s]
    src=(s[0],s[1])
    dst=(s[2],s[3])
    print('Obstacles position:',lst)
    G=grcr(src,dst,lst,size)
    Route=getShortestPath(G,src,dst,size)
    print('Route to move:',Route)
    # -----------------Shape of the Knight created here------------------------
    pos=vector(src[0],0,src[1])
    k1=cylinder(pos=pos+vector(0,0.3,0), axis=vector(0, 1, 0), radius=0.3,length=2.5)
    k5=sphere(pos=pos+vector(0, 3, 0), radius=0.6)
    k2=box(pos=pos+vector(0, 0.4, 0),size=vector(0.8,0.5,0.8))
    k3=cylinder(pos=pos+vector(0.5, 4, 0), axis=vector(-0.8, -1, 0), radius=0.05)
    k4=cylinder(pos=pos+vector(-0.5,4, 0), axis=vector(0.8, -1, 0), radius=0.05)
    k=compound([k1,k2,k3,k4,k5])
    k.shininess=0.2
    k.emissive=False
    k.texture='download.jpg'
    lst=Route
    for x in range(1,len(lst)):
        last=lst[x-1]
        current=lst[x]
        for xloc in np.linspace(last[0],current[0],100):
            k.pos=vector(xloc,2,last[1])
            rate(60)
        for yloc in np.linspace(last[1],current[1],100):
            k.pos=vector(xloc,2,yloc)
            rate(60)

def obstacles(s):
    s=int(s.text)
    global lst
    coords=generate_obstacle_coordinates(s,size)
    n=(size//2)+1
    print('coords',coords)
    print(size)
    print(n)
    for x in coords:
        y=(x[0],x[2])
        if y==dst or y==src:continue
        rate(20)
        pawn(vector(x[0],0.45,x[2]))
        y=(y[0]+(n),y[1]+(n))
        lst.append(y)
    print('Obstacles:',lst)


winput(bind=chess,text='Enter Dimension',width=200)  
scene.title_anchor
scene.append_to_caption('\n\n')
winput(bind=obstacles,text='No. of Obstacles',width=200)
scene.append_to_caption('    ')
winput(bind=s,text='Enter Source',width=200)

#Random Coordinates of pawn to be written here.\\\\\\\\\\\\\\\\\\\\\\\\\\\
# coords=generate_obstacle_coordinates(4)

while True:pass