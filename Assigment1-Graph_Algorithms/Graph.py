from copy import deepcopy
from random import randrange
from Exceptions import VertexError, EdgeError


def read_from_file(file_path):
    file = open(file_path, "r")

    if file == None:
        print("Nothing to see here!")
        return

    n, m = map(int, file.readline().split())
    g = DirectedGraph(n)
    for _ in range(m):
        vertex1, vertex2, edge_cost = map(int, file.readline().split())
        g.add_edge(vertex1, vertex2, edge_cost)
    file.close()
    return g

def write_to_file(graph, file_path):
    file = open(file_path, "w")

    file.write("{0} {1}\n".format(graph.count_vertices(), graph.count_edges()))

    for node in graph.vertices_iterator():
        for neighbour in graph.neighbors_iterator(node):
            file.write("{0} {1} {2}\n".format(node,
                                              neighbour,
                                              graph.get_edge_cost(node, neighbour)))
    file.close()


def random_graph(vertices_number, edges_number):
    g = DirectedGraph()

    for i in range(vertices_number):
        g.add_vertex(i)
    for j in range(edges_number):
        while True:
            vertex1 = randrange(vertices_number)
            vertex2 = randrange(vertices_number)
            if vertex1 != vertex2 and not g.is_edge(vertex1, vertex2):
                try:
                    g.add_edge(vertex1, vertex2, randrange(100))
                    break
                except EdgeError:
                    continue
    return g

class DirectedGraph:
    def __init__(self, n = 0, m = 0):
        self.__vertices = set()
        self.__neighbors = dict()
        self.__transposed = dict()
        self.__cost = dict()
        for i in range(n):
            self.add_vertex(i)
        for j in range(m):
            vertex1 = randrange(n)
            vertex2 = randrange(n)
            while self.is_edge(vertex1, vertex2):
                vertex1 = randrange(n)
                vertex2 = randrange(n)
            self.add_edge(vertex1, vertex2, randrange(100))

#iterators

    def vertices_iterator(self):
        for vertex in self.__vertices:
            yield vertex

    def neighbors_iterator(self, vertex):
        if not self.is_vertex(vertex):
            raise VertexError("This is not a vertex.")
        for neighbor in self.__neighbors[vertex]:
            yield neighbor

    def transposed_iterator(self, vertex):
        if not self.is_vertex(vertex):
            raise VertexError("This is not a vertex.")
        for neighbor in self.__transposed[vertex]:
            yield neighbor

    def edges_iterator(self):
        for key, value in self.__cost.items():
            yield key[0], key[1], value

    def is_vertex(self, vertex):
        return vertex in self.__vertices

    def is_edge(self, vertex1, vertex2):
        return vertex1 in self.__neighbors and vertex2 in self.__neighbors[vertex1]

    def count_vertices(self):
        return len(self.__vertices)

    def count_edges(self):
        return len(self.__cost)

    def in_degree(self, vertex):
        if vertex not in self.__transposed:
            raise VertexError("This one vertex you introduced is not a vertex here.")
        return len(self.__transposed[vertex])

    def out_degree(self, vertex):
        if vertex not in self.__neighbors:
            raise VertexError("This one vertex you introduced is not a vertex here.")
        return len(self.__neighbors[vertex])

    def get_edge_cost(self, vertex1, vertex2):
        if (vertex1, vertex2) not in self.__cost:
            raise EdgeError("We don't have this edge in our graph.")
        return self.__cost[(vertex1, vertex2)]

    def get_edge_Id(self, vertex1, vertex2):
        if (vertex1, vertex2) in self.__cost:
            return list(self.__cost.keys()).index((vertex1, vertex2))
        else:
            raise EdgeError("The specified edge does not exist.")

    def set_edge_cost(self, vertex1, vertex2, new_cost):
        if (vertex1, vertex2) not in self.__cost:
            raise EdgeError("We don't have this edge in our graph.")
        self.__cost[(vertex1, vertex2)] = new_cost

    def add_vertex(self, vertex):
        if self.is_vertex(vertex):
            raise VertexError("Cannot add a vertex more than once.")
        self.__vertices.add(vertex)
        self.__neighbors[vertex] = set()
        self.__transposed[vertex] = set()

    def add_edge(self, vertex1, vertex2, edge_cost=0):
        if self.is_edge(vertex1, vertex2):
            raise EdgeError("Cannot add an edge more than once.")
        if not self.is_vertex(vertex1) or not self.is_vertex(vertex2):
            raise EdgeError("These vertices on the edge do not exist.")
        self.__neighbors[vertex1].add(vertex2)
        self.__transposed[vertex2].add(vertex1)
        self.__cost[(vertex1, vertex2)] = edge_cost

    def remove_edge(self, vertex1, vertex2):
        if not self.is_edge(vertex1, vertex2):
            raise EdgeError("The specified edge does not exist.")

        del self.__cost[(vertex1, vertex2)]
        self.__neighbors[vertex1].remove(vertex2)
        self.__transposed[vertex2].remove(vertex1)

    def __str__(self):
            result = "Vertices: {}\n".format(self.count_vertices())
            result += "Edges:\n"
            for vertex1, vertex2, cost in self.edges_iterator():
                result += "({} -> {}) cost: {}\n".format(vertex1, vertex2, cost)
            return result

    def remove_vertex(self, vertex):

        if not self.is_vertex(vertex):
            raise VertexError("Cannot remove a vertex which doesn't exist.")

        to_remove = []

        for node in self.__neighbors[vertex]:
            to_remove.append(node)

        for node in to_remove:
            self.remove_edge(vertex, node)
        to_remove = []

        for node in self.__transposed[vertex]:
            to_remove.append(node)

        for node in to_remove:
            self.remove_edge(node, vertex)

        del self.__neighbors[vertex]
        del self.__transposed[vertex]
        self.__vertices.remove(vertex)

    def copy_graph(self):
        return deepcopy(self)

