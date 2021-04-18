class NetworkDiameter:
    """
    Class to find network diameter
    """

    def __init__(self):
        self.graph = {}
        self.diameter = -1

    def load_graph(self, data):
        """
        :param data: input data
        :return: graph
        """
        for path in data:
            key, value = path[0], path[1]
            self.graph.setdefault(key, []).append(value)
            key, value = path[1], path[0]
            self.graph.setdefault(key, []).append(value)
        return self.graph

    def find_diameter(self):
        """
        Go through all vertexes to find longest way
        :return: diameter of the graph
        -- O(N^2)
        """
        all_ways = []
        for vertex1 in self.graph.keys():
            for vertex2 in self.graph.keys():
                if vertex2 != vertex1:
                    result = self.pathFinder(vertex1, vertex2)
                    for path in result:
                        all_ways.append(len(path) - 1)
        self.diameter = max(all_ways)
        print(f"Diameter of network is {self.diameter}")

    def pathFinder(self, start, end, path=None):
        """
        Classic recursive Pass finder algorithm (Well, hello to my АИСД labs)
        ! Not work with cycles !
        :param start: Start vertex
        :param end: End vertex
        :param path: Current path (Start to End)
        :return: different
        -- O(1) ~ O(V + E)
        """
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.pathFinder(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths


if __name__ == "__main__":
    input_data = [[19, 45], [87, 25], [35, 73], [71, 50], [12, 23], [67, 39], [28, 47], [44, 59], [66, 92], [88, 74],
                  [77, 55], [72, 64], [18, 32], [90, 40], [39, 37], [93, 5], [43, 24], [99, 57], [48, 56], [51, 33],
                  [81, 44], [60, 29], [13, 34], [61, 82], [96, 75], [58, 81], [42, 76], [53, 32], [8, 97], [51, 93],
                  [45, 77], [46, 36], [21, 86], [91, 12], [8, 61], [73, 15], [70, 12], [45, 15], [33, 10], [56, 11],
                  [20, 38], [6, 80], [4, 7], [34, 89], [55, 22], [47, 16], [10, 67], [2, 85], [95, 44], [41, 31],
                  [17, 3],
                  [57, 20], [84, 80], [4, 98], [68, 83], [94, 23], [79, 97], [31, 18], [1, 12], [85, 78], [48, 15],
                  [4, 94],
                  [0, 10], [26, 2], [0, 9], [68, 49], [16, 40], [14, 69], [74, 86], [91, 62], [66, 85], [25, 44],
                  [36, 63],
                  [54, 14], [60, 36], [27, 68], [61, 50], [60, 49], [86, 82], [76, 6], [59, 54], [62, 65], [85, 17],
                  [48, 2], [14, 45], [72, 30], [72, 52], [37, 53], [72, 6], [75, 88], [24, 16], [46, 80], [65, 51],
                  [99, 13], [67, 20], [35, 33], [50, 64], [46, 93], [28, 96]]
    network = NetworkDiameter()
    graph = network.load_graph(input_data)
    # print(graph)
    network.find_diameter()

""" Requirements """

# Файл с решением первой задачи (диаметр сети без циклов) или архив с программой.
# Программа оценивается выше, чем решение на листочке.
# Если Вы сдаете программу, то приложите оценку сложности Ваших алгоритмов

# Сложность - O(N^2 * (|V|+|E|))
