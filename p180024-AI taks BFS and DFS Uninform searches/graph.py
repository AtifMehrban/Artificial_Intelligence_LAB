class Graph: 
    def __init__(self): 
        self.gr = {} 
        
    def add_node(self, node): 
        if node in self.gr: 
            raise ValueError("Node already in graph")
            
        self.gr[node] = [] 

    def add_edge(self, src, dest): 
        
        if src not in self.gr: 
            raise ValueError("Source node not in graph")
        if dest not in self.gr: 
            raise ValueError("Destination node not in graph")
            
        nexts = self.gr[src]
        if dest in nexts: 
            return 
        
        nexts.append(dest)
        
        
        #################################################
        
g = Graph() 

nodes = ['a', 'b', 'c', 'd', 'e', 'f'] 

for n in nodes: 
    g.add_node(n) 




edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('b', 'd'),
    ('c', 'd'),
    ('d', 'c'),
    ('e', 'f'),
    ('f', 'c')
]

for e in edges: 
    g.add_edge(e[0], e[1])
        
