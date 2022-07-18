from queue import Queue

dict_tree = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','F','G'],
    'F':['D','E','H'],
    'G':['E','H'],
    'H':['G','F']
}

visited = {}
level = {}
parent = {}
bfs_traversal_output = []

queue = Queue()

for node in dict_tree.keys():
    visited[node]=False
    level[node]= -1
    parent[node]=None

s='A'
visited[s]=True
level[s]=0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)
    for v in dict_tree[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]= level[u]+1
            queue.put(v)


print(bfs_traversal_output)
print(level)
print(parent)
