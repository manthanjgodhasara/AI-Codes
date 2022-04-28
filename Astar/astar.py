# A-STAR SEARCH : 

def display_2D(name, lst) :
  print("PRINTING {} : ".format(name)) 
  for i in range(len(lst)) : 
    print(lst[i])

n = int(input("Enter number of nodes : "))
e = int(input("Enter number of edges : "))

heuristics = [0] * (n+1)
edges = []
weights = []
visited = [0] * (n+1)

heuristics = [int(x) for x in input('Enter heuristics : ').split()]

print('heuristics', heuristics)
heuristics.insert(0, 0)

for i in range(n+1) : 
  edges.append([0] * (n+1))
  weights.append([0] * (n+1)) 

for i in range(e) : 
  e1 = int(input("Enter start node of edge {} : ".format(i+1)))
  e2 = int(input("Enter end node of edge {} : ".format(i+1)))
  w = int(input("Enter weight of edge {} : ".format(i+1)))
  edges[e1][e2] = 1
  weights[e1][e2] = w

display_2D('edges' , edges)
display_2D('weights', weights)

start = int(input("ENTER START NODE : "))
goal = int(input("ENTER GOAL NODE : "))

costs = {}
costs[start] = 0

open = []
closed = []

open.append(start)

while len(open) > 0 : 
  open = list(filter(lambda x : visited[x]==0, open))
  min_cost_node = open[0]
  for i in open : 
    if costs[i]+heuristics[i] < costs[min_cost_node] + heuristics[min_cost_node] : 
      min_cost_node = i  
    
  visited[min_cost_node] = 1


  for i in range(1, n+1) : 
    if edges[min_cost_node][i]==1 : 
      if visited[i] == 0 : 
        if i in open : 
          costs[i] = min(costs[i], costs[min_cost_node] + weights[min_cost_node][i]) 
        else : 
          costs[i] = costs[min_cost_node] + weights[min_cost_node][i]
          open.append(i)

      else : 
         if costs[i] > costs[min_cost_node] + weights[min_cost_node][i] : 
           open.append(i)
           closed.remove(i)
           costs[i] = costs[min_cost_node] + weights[min_cost_node] 
    
  open.remove(min_cost_node)
  closed.append(min_cost_node)

  if min_cost_node == goal : 
    print('goal reached, cost => {}'.format(costs[goal] + heuristics[goal]))
    break 
  
  print('**************************************')
  print('OPEN LIST -> ', open)
  print('CLOSED LIST -> ', closed)
  print('VISITED -> ', visited)
