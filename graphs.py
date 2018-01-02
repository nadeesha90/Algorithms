import pdb

class edge:
    def __init__(self,v1,v2,weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

class graph1:
    def __init__(self,nvertices):
        self.adj_mat = [[0 for i in range(nvertices)] for k in range(nvertices)]
        self.nvertices = nvertices
        
    def add_edge(self,vert1,vert2):
        self.adj_mat[vert1][vert2] = 1

class graph2:
    def __init__(self):
        self.adj_list = {}
        self.edges = {}

    def add_edge(self,vert1,vert2,weight=1):
        ef = edge(vert1,vert2,weight)
        #er = edge(vert2,vert1,weight)
        self._insert_edge(ef)
        #self._insert_edge(er)

    def _insert_edge(self,edge):
        v1,v2 = edge.v1,edge.v2
        self.edges[(v1,v2)] = edge

        if v1 in self.adj_list:
            self.adj_list[v1].append(v2)
        else:
            self.adj_list[v1] = [v2]

        if not(v2 in self.adj_list):
            self.adj_list[v2] = []

#    def _insert_edge(self,edge):
#        v1,v2 = edge.v1,edge.v2
#        
#        if v1 in self.adj_list:
#            self.adj_list[v1].append(edge)
#        else:
#            self.adj_list[v1] = [edge]
#
#        if not(v2 in self.adj_list):
#            self.adj_list[v2] = []

class stack:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self,item):
        self.arr.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.arr.pop()

class queue:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self,item):
        self.arr.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.arr.pop(0)

    def empty(self):
        return self.size == 0

def process_vertex(v):
    print 'process: {}'.format(v)

def discover_vertex(v):
    print 'discover: {}'.format(v)

def process_edge(v1,v2,colors):
    pass

def bfs1(G,source):
    Q = queue()    
    visited = []
    parent = {}
    Q.push(source)
    while not(Q.empty()):
        v1 = Q.pop()
        process_vertex(v)
        for v2 in G.adj_list[v1]:
            if not(v2 in visited):
                visited.append(v2)
                parent[v2] = v1
                Q.push(v2)

def bfs2(G,source):
    Q = queue()
    visited = []
    parent = {}
    Q.push(source)
    while not(Q.empty()):
        v1 = Q.pop()
        process_vertex(v1)
        verts = [i for i,v in enumerate(G.adj_mat[v1]) if v == 1]
        for v2 in verts:
            if not(v2 in visited):
                visited.append(v2)
                parent[v2] = v1
                Q.push(v2)

def bfs(G,source,visited):
    Q = queue()    
    parent = {}
    Q.push(source)
    visited.append(source)
    while not(Q.empty()):
        v1 = Q.pop()
        process_vertex(v1)
        for v2 in G.adj_list[v1]:
            process_edge(v1,v2)
            if not(v2 in visited):
                discover_vertex(v2)
                visited.append(v2)
                parent[v2] = v1
                Q.push(v2)

def dfs(G):
    visited = []
    for v in G.adj_list:
        if not(v in visited):
            dfs_recursive(G,v,visited)

def dfs_recursive(G,source,visited):
    process_vertex(source)
    for v in G.adj_list[source]:
        if not(v in visited):
            visited.append(v)
            dfs_recursive(G,v,visited)

def connected_components(G):
    visited = []
    cnt = 0
    for v in G.adj_list:
        if not v in visited:
            cnt += 1
            print "component: {}".format(cnt)
            bfs(G,v,visited)


def topological_sort(G):
    indegree = {}
    for v in G.adj_list:
        indegree[v] = 0

    for v in G.adj_list:
        for w in G.adj_list[v]:
            indegree[w] += 1 

    print "indegree: " + str(indegree) 

    s1 = [v for v in indegree if indegree[v] == 0]
    top_order = []

    while len(s1) > 0:
        v = s1.pop()
        top_order.append(v)
        #delete edges
        for w in G.adj_list[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                s1.append(w)
        
    print "topological order: " + str(top_order)

def dfs_top(G,a,order,visited):
    for b in G.adj_list[a]:
        if not (b in visited):
            visited.append(b)
            dfs_top(G,b,order,visited)
    order.append(a)

def topological_sort_dfs(G):
    s = []
    order = []
    visited = []

    for v in G.adj_list:
        if not (v in visited):
            dfs_top(G,v,order,visited)

    print "topological order: " + str(order)

def mst(G,s):
    intree = {v:False for v in G.adj_list}
    tree = []
    while intree[s] == False:
        intree[s] = True

        min_weight = 100
        min_edge = None
        for w in G.adj_list[s]:
            edge = G.edges[(s,w)]
            min_edge = min(min_edge,edge.weight) 

def dijkstra(G,s):
    dist = {v:100 for v in G.adj_list}
    intree = {v:False for v in G.adj_list}
    dist[s] = 0
    while intree[s]==False:
        intree[s] = True

        #explore each edge and update distance 
        for w in G.adj_list[s]:
            edge = G.edges[(s,w)]
            dist[w] = min(dist[w],dist[s]+edge.weight)

        min_dist = 100
        min_v = G.adj_list.keys()[1]

        #find vertex with minimum distance from source that hasn't been added to spanning tree yet
        for v in intree:
            if intree[v] == False and dist[v] < min_dist:
                min_v = v
                min_dist = dist[v]

        s = min_v
    
    print "dist: " + str(dist)

def two_coloring(G):
    color = {}
    
if __name__ == '__main__':
    G = graph2()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(3,4)
    G.add_edge(3,5)
    G.add_edge(2,5)

    print G.adj_list
    #connected_components(G)
    #topological_sort(G)
    #dfs(G)
    #dfs_recursive(G,0,[])

    #dijkstra(G,0)
    topological_sort_dfs(G)
