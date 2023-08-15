import heapq
from vpython import *
#BFS ALGORITHM:
def isvalid(pos,n):
    if (pos[0]>0 and pos[0]<=n) and (pos[1]>0 and pos[1]<=n):return True
    else:return False

def grcr(src,dst,lst,n):
    if src in lst or dst in lst:
        t=text(text='THIS MOVE IS NOT POSSIBLE', align='center', pos=vector(0,5,0), color=color.white)
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    gr={}
    q=[]
    visited=[]
    q.append(src)
    while q:
        
        t=q.pop(0)
        temp=[]
        for x in range(8):
            tpos=(t[0]+dx[x],t[1]+dy[x])
            if isvalid(tpos,n) and tpos not in lst:
                temp.append((tpos,1))
                if tpos not in visited:
                    visited.append(tpos)
                    q.append(tpos)
                if tpos==dst:break
        gr[t]=temp
        if tpos==dst:break
    gr[dst]=[]
    return gr


#Dijkstra's Algorithm

def getShortestPath(graph, start,dst,n):
    distances = {node: 10000000 for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    parent={}
    visited={node:False for node in graph}
    parent[start]=None
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if visited[current_node]:continue
        visited[current_node]=True
        for x in graph[current_node]:
            if x[0] not in graph:continue
            distance = current_distance + x[1]
            if distance < distances[x[0]]:
                distances[x[0]] = distance
                parent[x[0]]=current_node
                heapq.heappush(queue, (distance, x[0]))
    c=dst
    lst=[]
    if c not in parent:
        t=text(text='THIS MOVE IS NOT POSSIBLE', align='center', pos=vector(0,5,0), color=color.white)
        return[]
    while parent[c]!=None:
        lst.insert(0,parent[c])
        c=parent[c]
    lst.append(dst)
    x=(n//2)+1
    rerouted=[]
    for coordinates in lst:
        tup=(coordinates[0]-x,coordinates[1]-x)
        rerouted.append(tup)
    
    return rerouted
