# UNINFORMED SEARCH (D-F-S)
from collections import defaultdict
class Graph:
# Constructor
    def __init__(self):
        #default dictonary to store graph
        self.graph = defaultdict(list)
        # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v,visited):
        visited[v]= True
        print(v, end="")
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self,v):
        visited = [False]*(len(self.graph))
        self.DFSUtil(v,visited)
#Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print("Flowing is DFS from (starting from vertex 2)")
g.DFS(2)
