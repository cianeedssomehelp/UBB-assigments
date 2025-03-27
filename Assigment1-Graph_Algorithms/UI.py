from Graph import DirectedGraph, write_to_file, read_from_file

class Ui:
    def __init__(self, type_of_graph):
        self.graph = None
        self.type_of_graph = type_of_graph

    @staticmethod
    def print_menu():
        print("---------------------------------------------------------------")
        print("Here's what you can do with all these pesky graphs: ")
        print("---------------------------------------------------------------")
        print("1. Work with vertices.")
        print("2. Work with edges.")
        print("3. Create a random graph.")
        print("4. Copy the graph.")
        print("5. Read the graph from a file.")
        print("6. Write the graph to a file.")
        print("7. Print the graph.")
        print("0. Exit the program.")
        print("---------------------------------------------------------------")

    @staticmethod
    def edge_menu():
        print("============================================")
        print("Here's what you can do with edges: ")
        print("============================================")
        print("1. Get the cost of an edge.")
        print("2. Add an edge.")
        print("3. Remove an edge.")
        print("4. Modify the information attached to an edge.")
        print("5. Get the number of edges.")
        print("6. Check if the edge belongs to the graph.")
        print("7. Print the list of edges.")
        print("8. Print the neighbor list.")
        print("9. Print the transposed list.")
        print("10. Get the edge id of an edge.")
        print("0. Exit the edge operations.")
        print("============================================")

    @staticmethod
    def vertex_menu():
        print("============================================")
        print("Here's what you can do with vertices: ")
        print("============================================")
        print("1. Get the number of vertices.")
        print("2. Add a vertex.")
        print("3. Remove a vertex.")
        print("4. Given two vertices, find out whether there is an edge from the first one to the second one, and retrieve the Edge_id if there is an edge.")
        print("5. Get the in degree and the out degree of a specified vertex.")
        print("6. Print the list of vertices.")
        print("7. Check if the vertex belongs to the graph.")
        print("0. Exit the vertex operations.")
        print("============================================")

    @staticmethod
    def graph_menu():
        print("============================================")
        print("Here's what you can do with graphs generation: ")
        print("============================================")
        print("1. Generate an empty graph.")
        print("2. Generate a random graph with n vertices.")
        print("3. Generate a graph with n vertices and m random edges.")
        print("0. Exit the graph operations.")

    def copy_graph(self):
        self.graph = self.graph.copy_graph()
        print("The graph has been copied!")

    def print_graph(self):
        print(str(self.graph))

    def empty_graph(self):
        self.graph = self.type_of_graph()
        print("Now you have an empty graph!")

    def n_vertices_graph(self):
        vertices_number = input("How many vertices do you need: ")

        try:
            self.graph = self.type_of_graph(int(vertices_number))
            print("You got yourself a graph with {0} vertices!".format(vertices_number))
        except Exception as e:
            print(e)

    def random_graph(self):
        vertices_number = int(input("How many vertices would you like?\n> "))
        edges_number = int(input("How many edges would you like?\n> "))

        if edges_number > vertices_number * vertices_number:
            print("It is not possible to construct a graph with that many edges!")
            self.empty_graph()
        else:
            try:
                self.graph = self.type_of_graph(int(vertices_number),
                                                int(edges_number))
                print("Random Graph: Generated!")
            except Exception as e:
                print(e)

    def add_vertex(self):

        new_vertex = input("Type the vertex you wish to add: ")
        try:
            self.graph.add_vertex(int(new_vertex))
            print("The vertex {0} has been added.".format(new_vertex))
        except Exception as e:
            print(e)

    def add_edge(self):
        vertex1 = (input("Type the first vertex of the edge: "))
        vertex2 = input("Type the second vertex of the edge: ")
        cost = input("Type the cost of the edge: ")

        try:
            self.graph.add_edge(int(vertex1),
                                int(vertex2),
                                int(cost))
            print("The edge {0} {1} has been added.".format(vertex1, vertex2))

        except Exception as e:
            print(e)

    def remove_vertex(self):
        vertex_to_remove = input("Type the vertex you would like to remove: ")

        try:
            self.graph.remove_vertex(int(vertex_to_remove))
            print("The given vertex has been removed.")
        except Exception as e:
            print(e)

    def remove_edge(self):
        vertex1 = input("Type the first vertex of the edge: ")
        vertex2 = input("Type the second vertex of the edge: ")

        try:
            self.graph.remove_edge(int(vertex1), int(vertex2))
            print("The edge has been removed.")
        except Exception as e:
            print(e)

    def change_edge(self):
        vertex1 = input("Type the first vertex of the edge: ")
        vertex2 = input("Type the second vertex of the edge: ")
        cost = input("Type the cost of the edge: ")
        try:
            self.graph.set_edge_cost(int(vertex1), int(vertex2), int(cost))
        except Exception as e:
            print(e)

    def print_edge(self):
        vertex1 = input("Type the first vertex of the edge: ")
        vertex2 = input("Type the second vertex of the edge: ")
        try:
            print("The cost of the given edge is {0}.".format(self.graph.get_edge_cost(int(vertex1), int(vertex2))))
        except Exception as e:
            print(e)

    def in_degree(self):
        n = input("Type the vertex for which you wish to find the in degree: ")
        try:
            print(self.graph.in_degree(int(n)))
        except Exception as e:
            print(e)

    def out_degree(self):
        n = input("Type the vertex for which you wish to find the out degree: ")
        try:
            print(self.graph.out_degree(int(n)))
        except Exception as e:
            print(e)

    def count_vertices(self):
        print("There is a grand total of {0} vertices.".format(self.graph.count_vertices()))

    def count_edges(self):
        print("There is a grand total of {0} edges.".format(self.graph.count_edges()))

    def is_vertex(self):
        n = input("Type the vertex you wish to check: ")
        try:
            if self.graph.is_vertex(int(n)):
                print("The given vertex belongs to the graph!")
            else:
                print("The given vertex does not belong to the graph :(")
        except Exception as e:
            print(e)

    def is_edge(self):
        vertex1 = input("Type the first vertex of the edge: ")
        vertex2 = input("Type the second vertex of the edge: ")
        try:
            if self.graph.is_edge(int(vertex1), int(vertex2)):
                print(self.graph.get_edge_Id(int(vertex1), int(vertex2)))
                print("The given edge does exist in the graph!")
            else:
                print("The edge does not exist in the graph :(")
        except Exception as e:
            print(e)

    def print_vertex_list(self):
        for node in self.graph.vertices_iterator():
            print(node, end=" ")
        print()

    def print_neighbour_list(self):
        n = input("Type the vertex you wish to find neighbours for: ")
        try:
            anyone = False
            for node in self.graph.neighbors_iterator(int(n)):
                print(node, end=" ")
                anyone = True
            if not anyone:
                print("Vertex {0} has no neighbours.".format(n))
            else:
                print()
        except Exception as e:
            print(e)

    def print_transpose_list(self):
        n = input("Type the vertex you wish to find inbound neighbours for: ")
        try:
            anyone = False
            for node in self.graph.transposed_iterator(int(n)):
                print(node, end=" ")
                anyone = True
            if not anyone:
                print("Vertex {0} has no inbound neighbours.".format(n))
            else:
                print()
        except Exception as e:
            print(e)

    def print_edges(self):
        anyone = False
        for triple in self.graph.edges_iterator():
            print("Vertices {0}, {1} and cost {2}.".format(triple[0], triple[1], triple[2]))
            anyone = True
        if not anyone:
            print("There are no edges in the graph...")

    def get_edge_id(self):
        vertex1 = input("Type the first vertex of the edge: ")
        vertex2 = input("Type the second vertex of the edge: ")
        try:
            print("The edge id is {0}.".format(self.graph.get_edge_Id(int(vertex1), int(vertex2))))
        except Exception as e:
            print(e)

    def read_file(self):
        path = input("Type the file from which you wish to read: ")
        try:
            self.graph = read_from_file(path)
            print("The graph has been read from the file!")
        except Exception as e:
            print(e)

    def write_file(self):
        path = input("Type the file you wish to write to: ")
        try:
            write_to_file(self.graph, path)
            print("The graph has been saved to the file!")
        except Exception as e:
            print(e)
    def source(self):

        while True:
            self.print_menu()
            option = input("What would you like to do? > ")
            try:
                if option == "0":
                    print("Thank you for suffering along with us!")
                    break
                elif option == "1":
                    while True:
                        self.vertex_menu()
                        choice = input("What do you want to do? > ")
                        try:
                            if choice == "0":
                                break
                            elif choice == "1":
                                self.count_vertices()
                            elif choice == "2":
                                self.add_vertex()
                            elif choice == "3":
                                self.remove_vertex()
                            elif choice == "4":
                                self.is_edge()
                            elif choice == "5":
                                print("Here's the in degree of your vertex: ")
                                self.in_degree()
                                print("Here's the out degree of your vertex: ")
                                self.out_degree()
                            elif choice == "6":
                                self.print_vertex_list()
                            elif choice == "7":
                                self.is_vertex()
                            else:
                                raise Exception("Invalid input!")
                        except Exception as e:
                            print(e)
                elif option == "2":
                    while True:
                        self.edge_menu()
                        choice = input("What do you want to do? > ")
                        try:
                            if choice == "0":
                                break
                            elif choice == "1":
                                self.print_edge()
                            elif choice == "2":
                                self.add_edge()
                            elif choice == "3":
                                self.remove_edge()
                            elif choice == "4":
                                self.change_edge()
                            elif choice == "5":
                                self.count_edges()
                            elif choice == "6":
                                self.is_edge()
                            elif choice == "7":
                                self.print_edges()
                            elif choice == "8":
                                self.print_neighbour_list()
                            elif choice == "9":
                                self.print_transpose_list()
                            elif choice == "10":
                                self.get_edge_id()
                            else:
                                raise Exception("Invalid input!")
                        except Exception as e:
                            print(e)
                elif option == "3":
                    while True:
                        self.graph_menu()
                        choice = input("What do you want to do? > ")
                        if choice == "0":
                            break
                        if choice == "1":
                            self.empty_graph()
                        if choice == "2":
                            self.n_vertices_graph()
                        if choice == "3":
                            self.random_graph()
                elif option == "4":
                    self.copy_graph()
                elif option == "5":
                    self.read_file()
                elif option == "6":
                    self.write_file()
                elif option == "7":
                    self.print_graph()
                else:
                    raise Exception("Invalid input!")
            except Exception as e:
                print(e)

    def verifdeepcopy(self):
        self.graph = self.type_of_graph(6, 5)
        self.graph.add_edge(1, 2, 3)
        self.graph.add_edge(2, 3, 4)
        self.graph.add_edge(3, 4, 5)
        self.graph.add_edge(4, 5, 6)
        self.graph.add_edge(5, 1, 7)
        print("Graph: ")
        print(self.graph)

        copy = self.graph.copy_graph()
        print("Copy graph: ")
        print(copy)

        copy.add_edge(1, 3, 5)
        print("Initial graph: ")

        print(self.graph)
        print("Modified copy: ")
        print(copy)

        print(self.graph == copy)
        print(self.graph is copy)