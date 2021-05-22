# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import shortest_path
# #
# # graph = [
# # [0, 1, 2, 0],
# # [0, 0, 0, 1],
# # [2, 0, 0, 3],
# # [0, 0, 0, 0]
# # ]
#
# import numpy as np
#
#
# matrix_size = 10
#
# graph = np.random.uniform(0, 10, size=(matrix_size,matrix_size))
#
#
# import matplotlib.pyplot as plt
#
#
# plt.matshow(graph, cmap=plt.cm.Blues, vmin=0, vmax=matrix_size)
#
# for i in range(matrix_size):
#     for j in range(matrix_size):
#       c = graph[j,i]
#       plt.text(i, j, str(round(c)), va='center', ha='center')
#
# plt.show()
#
# graph = csr_matrix(graph)
# print(graph)
#
# dist_matrix, predecessors = shortest_path(csgraph=graph, directed=True, indices=0, return_predecessors=True)
#
# print(dist_matrix)
#
# print(predecessors)



########################################################################33
# from pathfinding.core.diagonal_movement import DiagonalMovement
# from pathfinding.core.grid import Grid
# from pathfinding.finder.a_star import AStarFinder
#
# matrix = [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 0, 0],
#   [1, 1, 1]
# ]
# grid = Grid(matrix=matrix)
#
# print(grid)
#
# start = grid.node(0, 0)
# end = grid.node(2, 3)
#
# finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
# path, runs = finder.find_path(start, end, grid)
#
# print('operations:', runs, 'path length:', len(path))
# print(grid.grid_str(path=path, start=start, end=end))

#
# import networkx as nx
# from matplotlib import pyplot as plt
#
# G = nx.grid_2d_graph(3,3)
#
# plt.figure(figsize=(6,6))
# pos = {(x,y):(y,-x) for x,y in G.nodes()}
# nx.draw(G, pos=pos,
#         node_color='lightgreen',
#         with_labels=True,
#         node_size=600)
#
#
#
# plt.show()
# coor1 = (0, 2) # seen as 2 in the arr array
# coor2 = (2, 1) # seen as 7 in the arr array
#
# rezultat = nx.bidirectional_shortest_path(G, source=coor1, target=coor2)
#
# print(rezultat)
#
#
# # [(0, 2), (1, 2), (2, 2), (2, 1)]

#########################################################

# A Naive recursive implementation of MCP(Minimum Cost Path) problem
import sys

R = 3
C = 3


# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C]
def minCost(cost, m, n):
        if (n < 0 or m < 0):
                return sys.maxsize
        elif (m == 0 and n == 0):
                return cost[m][n]
        else:
                return cost[m][n] + min(minCost(cost, m - 1, n - 1),
                                        minCost(cost, m - 1, n),
                                        minCost(cost, m, n - 1))


# A utility function that returns minimum of 3 integers */
def min(x, y, z):
        if (x < y):
                return x if (x < z) else z
        else:
                return y if (y < z) else z


# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]

# print(cost)

import numpy as np

dimensions = 3

# cost = np.random.uniform(1, 10, size=(4,4)).tolist()

print(cost)

print(minCost(cost, dimensions - 1, dimensions - 1))
# This code is contributed by
# Smitha Dinesh Semwal