# Algorithms and data structures

This repository shows the exploration of algorithms and data structures in different programming languages. My goal is to create a summary of major findings and implementations. Some of the implementations here are a re-exploration of topics and already know about, but will include new lessons learned about best practices and programming techniques. 


## Sorting algorithms

## Graphs

Graphs are data structures defined by nodes (also called vertices) and edges. Edges connect two nodes
to each other. Graphs are the canonical representation of networks and can
be used for a wide variety of purposes such as finding the shortest/largest path,
find the connected regions in a network, or getting instructions about how to
move from point A to point B. There are two fundamental algorithms used to
traverse a graph (search): one es Breath First Search (a.k.a. BFS) which goes layer by layer.
The second one is Depth First Search (a.k.a. DFS), which traverses the networy by recursively going to the
deepest layer and coming back.
The generic graph search algorithm consists of a two step goal:
1. Find everything findable from a given start vertex
2. Don't explore anything twice
Generally with time complexity `O(m+n)`, `m` the number of vertices and `n` the 
number of edges explored.
And these are the fundalmental ideas followed in the BFS and DFS, the difference
being how the graph is traversed every time a new node (vertex) is explored. 

### BFS (Breath First Search)

### DFS (Depth Fisrt Search)

## Misc

### Hangman

### Card deck 
