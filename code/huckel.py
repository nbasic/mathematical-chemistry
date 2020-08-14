#!/usr/bin/env python3
import networkx
import numpy.linalg
import matplotlib.pyplot

# There are several ways to create a graph with networkx.

# Creating a graph that belongs to a known family (e.g. complete
# graphs, path graphs, etc.).
#
# g = networkx.complete_graph(6)
# g = networkx.cycle_graph(6)
# g = networkx.path_graph(6)
# g = networkx.star_graph(6)

# Create a graph by listing its edges.
#
g = networkx.Graph([(1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (5, 7)])

# Create a graph by specifying its graph6 string.
#
# graph6_code = 'N??CA?_C?OOOP?[?T??'
# g = networkx.from_graph6_bytes(bytes(graph6_code, 'ascii'))

# Drawing graphs using Matplotlib
#
# networkx.draw(g)
# matplotlib.pyplot.show()

# We get the adjacency matrix of the graph (in the numpy format)
# and then determine its eigenvalues and eigenvectors using numpy.

a = networkx.to_numpy_matrix(g)  # Adjacency matrix for numpy
eigval, eigvec = numpy.linalg.eigh(a)

for i in range(len(eigval)):
	# Display i-th eigenvalue
	print('Eigenvalue:', eigval[i])
	# Display eigenvector of the i-th eigenvalue
	print('Eigenvector:', numpy.transpose(eigvec[:, i]))
	print()
