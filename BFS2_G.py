graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C', 'H'],
    'G': ['C'],
    'H': ['F']
}

def BFS(graph,start,dest) : 
    global flaag                      
    flaag = 0
    queue = list()
    visited = list()
    queue.append(start)
    print('Visited', start)
    result = ["Not reachable", list()]

    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node==dest:
            print('Destination node found',node)
            result[0] = 'Reachable'
            flaag=1
            break
        print(node,'Is not a destination node')
        for child in graph[node]:
            if child not in visited:
                queue.append(child)

    result[1] = visited 
    return result

result = BFS(graph, "A", "C")
print(result[0])
print("Path used to traverse :-" , result[1])
print(flaag)