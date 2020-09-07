# Python program for Bellman-Ford's single source
# shortest path algorithm.
import time
from collections import defaultdict

from random import random, randint

import copy


# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph
        self.vertexInfo = []

    # function to add an edge to graph
    def addEdge(self, u, v, bus_weight, train_weight):
        self.graph.append([u, v, bus_weight, train_weight])

    def addVertex(self, transfer_time):
        bus = False
        train = False
        self.vertexInfo.append([transfer_time, bus, train, []])

        # utility function used to print the solution

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))
            print("Shortest path for vertex:", i, " is ", self.vertexInfo[i][3])

            # The main function that finds shortest distances from src to

    # all other vertices using Bellman-Ford algorithm.  The function
    # also detects negative weight cycle
    def BellmanFord(self, src, target):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        # d[s] ← 0
        # for each v ∈ V – {s}
        # do d[v] ← ∞
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges

        # for i ← 1 to | V | – 1
        # do for each edge(u, v) ∈ E
        # do if d[v] > d[u] + w(u, v)
        # then d[v] ← d[u] + w(u, v)

        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, bus_weight, train_weight in self.graph:
                if u == 0:
                    if dist[u] != float("Inf") and dist[u] + bus_weight < dist[v] and bus_weight != 0:
                        self.vertexInfo[v][1] = True
                        self.vertexInfo[v][2] = False
                        dist[v] = dist[u] + bus_weight
                    if dist[u] != float("Inf") and dist[u] + train_weight + self.vertexInfo[0][0] < dist[
                        v] and train_weight != 0:
                        self.vertexInfo[v][1] = False
                        self.vertexInfo[v][2] = True
                        dist[v] = dist[u] + train_weight + self.vertexInfo[0][0]
                    if self.vertexInfo[v][1] is True or self.vertexInfo[v][2] is True:
                        self.vertexInfo[v][3].append(u)
                else:
                    if dist[u] != float("Inf") and dist[u] + bus_weight < dist[v]:
                        # dist[v] = dist[u] + train_weight
                        if dist[u] != float("Inf") and self.vertexInfo[u][1] is False and dist[u] + bus_weight + \
                                self.vertexInfo[u][0] < dist[v]:
                            self.vertexInfo[v][1] = True
                            self.vertexInfo[v][2] = False
                            if u != 0:
                                if u not in self.vertexInfo[v][3]:
                                    self.vertexInfo[v][3].append(u)
                                dist[v] = dist[u] + bus_weight + self.vertexInfo[u][0]
                            else:
                                dist[v] = dist[u] + bus_weight
                        elif dist[u] != float("Inf") and self.vertexInfo[u][1] is True and dist[u] + bus_weight < dist[
                            v]:
                            if u not in self.vertexInfo[v][3]:
                                self.vertexInfo[v][3].append(u)
                            dist[v] = dist[u] + bus_weight

                    if dist[u] != float("Inf") and dist[u] + train_weight < dist[v]:
                        # dist[v] = dist[u] + train_weight
                        if dist[u] != float("Inf") and self.vertexInfo[u][2] is False and dist[u] + train_weight + \
                                self.vertexInfo[u][0] < dist[v]:
                            self.vertexInfo[v][1] = False
                            self.vertexInfo[v][2] = True
                            if u != 0:
                                if u not in self.vertexInfo[v][3]:
                                    self.vertexInfo[v][3].append(u)
                                dist[v] = dist[u] + train_weight + self.vertexInfo[u][0]
                            else:
                                dist[v] = dist[u] + train_weight
                        elif dist[u] != float("Inf") and self.vertexInfo[u][2] is True and dist[u] + train_weight < \
                                dist[v]:
                            if u not in self.vertexInfo[v][3]:
                                self.vertexInfo[v][3].append(u)
                            dist[v] = dist[u] + train_weight

                    # Step 3: check for negative-weight cycles.  The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.

        # for each edge(u, v) ∈ E
        # do if d[v] > d[u] + w(u, v)
        # then report
        # that a negative - weight cycle exists

        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, bus_weight, train_weight in self.graph:
                if u == 0:
                    if dist[u] != float("Inf") and dist[u] + bus_weight + self.vertexInfo[u][0] < dist[v]:
                        print("Graph contains negative weight cycle")
                        return
                    if dist[u] != float("Inf") and dist[u] + train_weight + self.vertexInfo[u][0] < dist[v]:
                        print("Graph contains negative weight cycle")
                        return
                else:
                    if dist[u] != float("Inf") and dist[u] + bus_weight + self.vertexInfo[u][0]< dist[v]:
                        # dist[v] = dist[u] + train_weight
                        if dist[u] != float("Inf") and self.vertexInfo[u][1] is False and dist[u] + bus_weight + \
                                self.vertexInfo[u][0] < dist[v]:
                            self.vertexInfo[v][1] = True
                            self.vertexInfo[v][2] = False
                            if u != 0:
                                print("Graph contains negative weight cycle")
                                return
                            else:
                                print("Graph contains negative weight cycle")
                                return
                        elif dist[u] != float("Inf") and self.vertexInfo[u][1] is True and dist[u] + bus_weight + self.vertexInfo[u][0] < dist[
                            v]:
                            print("Graph contains negative weight cycle")
                            return

                    if dist[u] != float("Inf") and dist[u] + train_weight + self.vertexInfo[u][0]< dist[v]:
                        # dist[v] = dist[u] + train_weight
                        if dist[u] != float("Inf") and self.vertexInfo[u][2] is False and dist[u] + train_weight + \
                                self.vertexInfo[u][0] < dist[v]:
                            self.vertexInfo[v][1] = False
                            self.vertexInfo[v][2] = True
                            if u != 0:
                                print("Graph contains negative weight cycle")
                                return
                            else:
                                dist[v] = dist[u] + train_weight
                        elif dist[u] != float("Inf") and self.vertexInfo[u][2] is True and dist[u] + train_weight < \
                                dist[v]:
                            print("Graph contains negative weight cycle")
                            return

        # print all distance
        # At the end, d[v] = δ(s, v),
        # if no negative-weight cycles.
        for a in range(self.V):
            if a == 0:
                self.vertexInfo[a][3].append(0)
            elif a != 0:
                myindex = self.vertexInfo[a][3][-1]
                self.vertexInfo[a][3] = (self.vertexInfo[myindex][3]).copy()
                self.vertexInfo[a][3].append(a)

        self.printArr(dist)
        print(dist[target])
        print(self.vertexInfo[target][3])





g = Graph(5)
for i in range(5):
    g.addVertex(randint(0, 10))
g.addEdge(0, 1, randint(0, 10), randint(0, 10))
g.addEdge(0, 2, randint(0, 10), randint(0, 10))
g.addEdge(1, 2, randint(0, 10), randint(0, 10))
g.addEdge(1, 3, randint(0, 10), randint(0, 10))
g.addEdge(1, 4, randint(0, 10), randint(0, 10))
g.addEdge(2, 3, randint(0, 10), randint(0, 10))
g.addEdge(4, 3, randint(0, 10), randint(0, 10))


# Print the solution
g.BellmanFord(0, 3)
time_start = time.perf_counter()
time_elapsed = (time.perf_counter() - time_start)
print(time_elapsed)
