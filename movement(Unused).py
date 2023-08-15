from vpython import *
from time import *
import numpy as np

n=8
for i in range(1,n+1):
     for j in range(1,n+1):
         if (i+j) % 2 == 1:
             sColor = color.black
         else: sColor = color.white
         box(pos=vector(i,0.1,j),length=1,height=0.1,width=1,color=sColor)


piece=box(pos=vector(1,2.1,2),size=vector(0.7,4,0.7), color=color.cyan)

lst=[(1,2),(8,8),(5,5)]

for y in lst:
    box(pos=vector(y[0],0.1,y[1]), size=vector(0.1,6,0.1),color=color.white)

for x in range(1,len(lst)):
    last=lst[x-1]
    current=lst[x]
    for xloc in np.linspace(last[0],current[0],50):
        piece.pos=vector(xloc,2,last[1])
        rate(10)
    for yloc in np.linspace(last[1],current[1],50):
        piece.pos=vector(xloc,2,yloc)
        rate(60)

while True:pass