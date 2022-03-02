from collections import defaultdict
class Grafo:
    def __init__(self,vertices):
        self.grafo = defaultdict(list) 
        self.V = vertices 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def busqueda(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.busqueda(i,visited,stack)

        stack.insert(0,v)

  
    def busquedatopologica(self):
        visited = [False]*self.V
        stack =[]
        for i in range(self.V):
            if visited[i] == False:
                self.busqueda(i,visited,stack)
        print (stack)
