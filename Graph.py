class Graph(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 1 
            self.adj[dest-1][orig-1] = 1 
        
    def remove_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 0 
            self.adj[dest-1][orig-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print() 
            for val in row: 
                print('{:4}'.format(val),end="") 

#a sample Graph 
G = Graph(4) 
G.add_edge(1, 3) 
G.add_edge(3, 4)
G.add_edge(2, 4)
G.display()