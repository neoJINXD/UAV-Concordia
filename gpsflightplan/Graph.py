class Node:
    '''Class for a node, a vertex in the graph'''
    def __init__(self, vertex, xpos, ypos):
        self.id = vertex
        self.x = xpos
        self.y = ypos
        self.adj = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adj])

    def add_neighbour(self, neighbour):
        '''Adds a neighbour to the node while autocalculating the weight as the distance'''
        def get_node_distance(start, end):
            # Pythagorus theorem to get distance between 2 points
            distance = (((end.x - start.x) ** 2) + ((end.y - start.y) ** 2)) ** 0.5
            return distance

        self.adj[neighbour] = get_node_distance(self, neighbour)

    def get_connections(self):
        '''Gets all the neighbours of a given node'''
        return self.adj.keys()

    def get_id(self):
        '''Gets the name for the node'''
        return self.id

    def get_weight(self, neighbour):
        '''Gets the weight/distance to a specific node that is a neighbour'''
        return self.adj[neighbour]


class Graph:
    def __init__(self):
        self.vertex_dict = {}

    def __iter__(self):
        return iter(self.vertex_dict.values())

    def add_vertex(self, node, xpos, ypos):
        '''Adds a vertex of type node to the graph'''
        newV = Node(node, xpos, ypos)
        self.vertex_dict[node] = newV
        return newV

    def get_vertex(self, node):
        '''Gets the specified node, by id'''
        return self.vertex_dict[node]

    def add_edge(self, start, end):
        '''Adds an edges between two nodes
           Must go both ways since undirected graph'''
        # Undirected, so needs connection to and from
        self.vertex_dict[start].add_neighbour(self.vertex_dict[end])
        self.vertex_dict[end].add_neighbour(self.vertex_dict[start])

    def get_vertices(self):
        '''Gets all the vertices in a graph'''
        return self.vertex_dict.keys()

#Main to test making a graph
if __name__ == '__main__':
    g = Graph()

    g.add_vertex('a', 0.7, 0.7)
    g.add_vertex('b', 3, 49)
    g.add_vertex(1, 576, 5)

    g.add_edge('a', 'b')
    g.add_edge('a', 1)

    for i in g:
        for j in i.get_connections():
            s = i.get_id()
            e = j.get_id()
            print('(%s, %s, %3d)' % (s, e, i.get_weight(j)))
