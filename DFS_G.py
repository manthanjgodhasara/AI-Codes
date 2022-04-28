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

visited = list() # Set to keep track of visited nodes of graph.
result=list()

def dfs(visited, graph, node,dest):  #function for dfs 
    if node==dest:
        return result
    if node not in visited:
        result.append(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour,dest)
    return result

# Driver Code
print("Following is the Depth-First Search")
print(dfs(visited, graph, 'A','F'))