n = int(input("Enter no. of nodes: "))
e = int(input("Enter no. of edges: "))
edges=[]
cost = []
vis=[]
selected={1:0}
for i in range(0,n+1):
  edges.append([0] * (n+1))
  cost.append([0] * (n+1))
  vis.append(0)
for i in range(0,e):
  temp = [int(x) for x in input("Enter start node,end node and weight ofedge %d: " %(i+1)).split()]
  edges[temp[0]][temp[1]] = 1
  cost[temp[0]][temp[1]] = temp[2]
print("\nADJACENCY MATRIX")
for i in range(0,n+1):
  print(*edges[i])
print("\nWEIGHT MATRIX")
for i in range(0,n+1):
  print(*cost[i])
start = int(input("\nEnter the start node: "))
end = int(input("Enter the end node: "))
openlst=[1]
closelst=[]
dct = {0:1} #{g:node}
cnt=2
print("\nIteration 1 : OPEN LIST =",openlst,"\t\t\tCLOSE LIST =",closelst)
while(1):
    smallest = min(dct)
    curr = dct[smallest]
    closelst.append(curr)
    openlst.remove(curr)
    dct.pop(smallest)
    selected[curr]=smallest
    vis[curr]=1

    if(curr==end):
      break
    for j in range(0,n+1):
      if(edges[curr][j]==1 and vis[j]==0):
        tcost = cost[curr][j] + selected[list(selected)[-1]]
        dct[tcost]=j
        openlst.append(j)
        print("Iteration",cnt,": OPEN LIST =",openlst,"\t\tCLOSE LIST=",closelst)
    cnt+=1

print("Iteration",cnt,": OPEN LIST =",openlst,"\t\tCLOSE LIST =",closelst)
print("\nExplored:",end=" ")

for i in range(0,len(closelst)-1):
    print(closelst[i],end="-->")
print(closelst[len(closelst)-1])
print('\nCOST =',smallest)

'''
7
10
1 2 5
1 4 3
2 3 1
2 5 4
3 5 6
3 7 8
4 5 2
4 6 2
5 7 4
6 7 3
'''
