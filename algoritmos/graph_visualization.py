import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self, color_dict):
        print(color_dict)
        G = nx.Graph()
        G.add_edges_from(self.visual)
        color_map = []
        for node in G:
            #print(frequencies[node])
            color_map.append(color_dict[node])
            print(f"frequencies {frequencies[node]} color: {colors[node]}")

        nx.draw_networkx(G, node_color=color_map, with_labels=True)
        plt.show()


frequencies = {
    0: "1.70 to 2.60 GHz",
    1: "18.0 to 26.5 GHz",
    2: "2.20 to 3.30 GHz",
    3: "26.5 to 40.0 GHz",
    4: "2.60 to 3.95 GHz",
    5: "33 to 50 GHz",
    6: "3.30 to 4.90 GHz",
    7: "40 to 60 GHz",
    8: "3.95 to 5.85 GHz",
    9: "40 to 75 GHz",
    10: "4.90 to 7.05 GHz",
    11: "60 to 90 GHz",
    12: "5.85 to 8.20 GHz",
    13: "75 to 110 GHz",
    14: "7.05 to 10.10 GHz",
    15: "90 to 140 GHz",
    16: "8.2 to 12.4 GHz",
    17: "110 to 170 GHz",
    18: "12.4 to 18.0 GHz",
    19: "325 to 500 GHz"}

colors = {
    0: '#e6194B',
    1: '#3cb44b',
    2: '#ffe119',
    3: '#4363d8',
    4: '#f58231',
    5: '#911eb4',
    6: '#42d4f4',
    7: '#f032e6',
    8: '#bfef45',
    9: '#fabed4',
    10: '#469990',
    11: '#dcbeff',
    12: '#9A6324',
    13: '#fffac8',
    14: '#800000',
    15: '#aaffc3',
    16: '#808000',
    17: '#ffd8b1',
    18: '#000075',
    19: '#a9a9a9'}