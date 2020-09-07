from random import randint
import sys
sys.setrecursionlimit(1500)


def findEdges(mat, vertex):
    edgeList = []
    for i in range(len(mat)):
        if mat[i][vertex] == 1:
            edgeList.append(i)
    return edgeList


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.adjacency_matrix = [[0, 1, 1, 1],
                                 [0, 0, 1, 1],
                                 [0, 1, 0, 1],
                                 [0, 0, 1, 0]]  # default dictionary to store graph
        self.bus_weights = [[0, randint(1, 10), randint(1, 10), randint(1, 10)],
                            [0, 0, randint(1, 10), randint(1, 10)],
                            [0, randint(1, 10), 0, randint(1, 10)],
                            [0, 0, randint(1, 10), 0]]
        self.train_weights = [[0, randint(1, 10), randint(1, 10), randint(1, 10)],
                              [0, 0, randint(1, 10), randint(1, 10)],
                              [0, randint(1, 10), 0, randint(1, 10)],
                              [0, 0, randint(1, 10), 0]]
        self.vertexInfo = [[randint(1, 10), False, False], [randint(1, 10), False, False],
                           [randint(1, 10), False, False], [randint(1, 10), False, False]]
        self.my = []

    def Func(self, src, trgt):
        dist = [-1] * 4
        dist[src] = 0

        if src == 0 and trgt == 0:
            return 0
        else:
            if trgt != 0:
                mylist = findEdges(self.adjacency_matrix, trgt)
            for u in mylist:

                if self.vertexInfo[u][1] is False and self.vertexInfo[u][2] is False:
                    if self.bus_weights[u][trgt] <= self.train_weights[u][trgt] + self.vertexInfo[u][0]:
                        self.vertexInfo[trgt][1] = True
                        distance = self.Func(0, u) + self.bus_weights[u][trgt]
                    else:
                        self.vertexInfo[trgt][2] = True
                        distance = self.Func(0, u) + self.train_weights[u][trgt]
                elif self.vertexInfo[u][1] is True:  # Bus is true
                    if self.bus_weights[u][trgt] < self.train_weights[u][trgt] + self.vertexInfo[u][0]:
                        distance = self.Func(0,u) + self.bus_weights[u][trgt]
                    else:
                        self.vertexInfo[trgt][2] = False
                        distance = self.Func(0, u) + self.train_weights[u][trgt] + self.vertexInfo[u][0]
                elif self.vertexInfo[u][2] is True:  # Train is true
                    if self.train_weights[u][trgt] < self.bus_weights[u][trgt] + self.vertexInfo[u][0]:
                        distance = self.Func(0, u) + self.train_weights[u][trgt]
                    else:
                        self.vertexInfo[trgt][2] = False
                        distance = self.Func(0, u) + self.bus_weights[u][trgt] + self.vertexInfo[u][0]
            self.my.append(distance)


g = Graph(4)
print(g.Func(0, 3))
