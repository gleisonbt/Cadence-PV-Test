from collections import deque

# Using a Python dictionary to act as an adjacency list
graph = {
    '1' : ['3','2','4'],
    '2' : ['3','6'],
    '3' : ['6'],
    '4' : ['5'],
    '5' : [],
    '6' : ['7', '8'],
    '7' : ['10'],
    '8' : ['6','9'],
    '9' : ['10'],
    '10' : ['11'],
    '11' : [],
}


visited = set() # Set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for next in graph[node]:
            dfs(visited, graph, next) #recursion


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        print(path)
    for node in graph[start]:
        if node not in path:
            newpath = find_all_paths(graph, node, end, path)
            if newpath: 
                print(newpath)

#BFS [Breadth First Search]
def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    queue = deque(start)
    while len(queue):
        at = queue.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at]+ [next]
                q.append(next)
    print(dist.get(end))
    
    
# Driver Code
dfs(visited, graph, '1')
find_all_paths(graph, '1', '11')
find_shortest_path(graph, '1', '11')
