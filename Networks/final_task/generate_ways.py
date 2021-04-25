from collections import defaultdict

N = 838
M = 857
def find_all_paths(graph):


    for i in range(M):
        for j in range(1, N):
            if i == 0:
                graph[i][j] = graph[i][j-1]
            else:
                graph[i][j] = graph[i-1][j-1] + graph[i-1][j] + graph[i][j - 1]
    print(graph)
    print(graph[M-1][N-1])


def generate_all_Ways():

    _graph = [[1 for x in range(N)] for y in range(M)]
    return _graph


if __name__ == "__main__":
    graph = generate_all_Ways()
    find_all_paths(graph)
