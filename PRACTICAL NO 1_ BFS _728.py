# PRACTICAL NO.1: UNINFORMED SEARCH(B-F-S)
# Python3 Program to print BFS traversal
#from a given sourse vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
# this class represents a directed graph
# using adjacency list representation
class Graph:
    #Constructor
    def __init__(self) :
        #default dictionary to store graph
        self.graph = defaultdict(list)

    #function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

        # Function to print a BFS of graph
    def BFS(self, s) :
        # Mark all the vettices as not visited
        visited = [False] * (len(self.graph))

        #Create a queue for BFS
        queue = []


        # Mark the sourse node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
                s = queue.pop(0)
                print (s, end = "")

                # Get all adjacent vertices of the
                # dequeued vertex s. If a adjacent
                # has not been visited, then mark it
                # visited and enqueue it
                for i in self.graph[s] :
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True

#Drive code
# create a graph given in the diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Flowing is Breadth First Traversal(Starting from vertex 2)")
g.BFS(2)
