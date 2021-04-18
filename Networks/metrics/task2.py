from queue import *


class NetworkDiameter:
    """
    New class to find network diameter
    """

    def __init__(self):
        self.graph = {}
        self.n = 0
        self.matrix = None
        self.visited = {}
        self.diameter = -1

    def load_graph(self, data):
        """
        :param data: input data
        :return: graph
        """
        self.n = len(data)
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]  # double array
        for path in data:
            key, value = path[0], path[1]
            self.graph.setdefault(key, []).append(value)
            key, value = path[1], path[0]
            self.graph.setdefault(key, []).append(value)
        return self.graph

    def find_diameter(self):
        """
        New realisation to find diameter.
        Classic algorithm with matrix is used. (Well, second hello to my АИСД labs)
        :return: diameter of the graph
        """
        # Matrix prepare
        for i in range(self.n):
            for j in range(self.n):
                self.matrix[i][j] = -1
        for s in self.graph.keys():
            # Visited vertex prepare
            for v in self.graph.keys():
                self.visited[v] = False
            # Queue of vertex to be visited
            Q = Queue(maxsize=0)
            # Start is already visited
            self.visited[s] = True
            Q.put(s)
            self.matrix[s][s] = 0
            while not Q.empty():
                v = Q.get()
                for w in self.graph[v]:
                    if not self.visited[w]:
                        self.visited[w] = True
                        # Move through all vertexes incrementing value of distance to construct way
                        self.matrix[s][w] = self.matrix[s][v] + 1
                        Q.put(w)
        # Go through all distances in matrix to find longest
        for line in self.matrix:
            line.append(self.diameter)
            self.diameter = max(line)
        print(f"Diameter of network is {self.diameter}")


if __name__ == "__main__":
    input_data = [[22, 36], [58, 6], [68, 21], [66, 14], [17, 9], [25, 65], [47, 71], [53, 10], [37, 4], [16, 8],
                  [73, 40], [24, 74], [12, 67], [55, 0], [8, 15], [50, 73], [65, 74], [26, 34], [35, 57], [41, 51],
                  [32, 43], [69, 34], [58, 42], [26, 7], [27, 55], [70, 74], [12, 29], [44, 39], [59, 35], [61, 51],
                  [31, 72], [4, 65], [45, 16], [19, 10], [66, 1], [63, 69], [63, 18], [66, 21], [48, 57], [54, 3],
                  [56, 16], [61, 64], [55, 5], [70, 73], [44, 51], [62, 30], [63, 38], [47, 72], [46, 33], [28, 30],
                  [2, 9], [8, 48], [4, 0], [49, 13], [13, 1], [24, 26], [32, 36], [71, 60], [22, 28], [36, 54],
                  [19, 11], [67, 71], [30, 33], [36, 25], [6, 49], [20, 32], [52, 64], [63, 53], [45, 38], [23, 31],
                  [9, 18], [0, 51], [18, 29], [14, 74], [49, 58], [61, 26], [51, 53], [12, 38], [49, 10], [13, 48],
                  [53, 17], [21, 35], [1, 72], [71, 29], [33, 65], [39, 5], [31, 44], [49, 50], [1, 61], [4, 26],
                  [17, 35], [64, 59], [51, 71], [30, 71], [60, 39], [54, 65], [51, 28], [30, 36], [39, 63], [50, 5],
                  [7, 48], [64, 45], [46, 47], [58, 74], [60, 40], [44, 16], [67, 15], [64, 35], [9, 38], [54, 72],
                  [40, 49], [44, 71], [39, 49], [74, 6], [67, 29], [46, 73], [2, 70], [24, 17], [18, 40], [9, 65],
                  [1, 0], [16, 67], [37, 53], [58, 4], [12, 49], [26, 52], [0, 65], [51, 25], [27, 1], [41, 67],
                  [39, 57], [12, 9], [41, 32], [62, 16], [19, 50], [40, 13], [72, 42], [44, 14], [64, 12], [17, 61],
                  [24, 1], [69, 25], [9, 46], [9, 39], [35, 36], [72, 62], [17, 71], [63, 41], [66, 13], [50, 26],
                  [35, 20], [17, 14], [4, 41], [57, 63], [58, 57], [41, 12], [53, 63], [54, 2], [21, 51], [14, 39],
                  [50, 68], [53, 29], [9, 19], [25, 29], [39, 20], [63, 10], [11, 35], [19, 26], [1, 11], [22, 18],
                  [2, 40], [67, 39], [44, 19], [66, 43], [62, 25], [74, 55], [2, 22], [46, 22], [57, 12], [10, 31],
                  [57, 7], [50, 65], [29, 51], [31, 11], [19, 49], [36, 11], [46, 34], [68, 59], [27, 61], [21, 2],
                  [19, 20], [5, 14], [19, 56], [4, 35], [5, 46], [28, 16], [64, 6], [17, 6], [64, 74], [53, 48],
                  [68, 46], [41, 67], [44, 35], [24, 9], [48, 61], [63, 38], [40, 0], [60, 0], [8, 17], [26, 74],
                  [58, 72], [9, 23], [7, 39], [31, 68], [43, 31], [65, 19], [45, 1], [68, 27], [43, 74], [24, 40],
                  [62, 70], [28, 50], [70, 38], [23, 74]]
    network = NetworkDiameter()
    graph = network.load_graph(input_data)
    # print(graph)
    network.find_diameter()

"""Requirements"""

# Файл с решением второй задачи (диаметр произвольной сети) или архив с программой.
# Программа оценивается выше, чем решение на листочке.
# Если Вы сдаете программу, то приложите оценку сложности Ваших алгоритмов

# Сложность - O(N^3)
