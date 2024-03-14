# Algorithms and data structures

In this repository I explore algorithms and data structures in different programming languages. My goal is to create a summary of major findings and implementations. Some of the implementations here are a re-exploration of topics and already known about in the past, but will include new lessons learned about best practices and programming techniques. 


## Sorting algorithms

### Bubble sort

### Insertion sort 

### Mergesort

### Quicksort

### More
[Here](https://www.toptal.com/developers/sorting-algorithms) is a visualization of different sorting algorithms with its speed in different conditions. 
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

- Explore nodes in "layers".
- The graph is traversed by FIFO sequence (First In First Out): every vortex
in one layer is explored before to the next one.
- The queue is the natural data structure to follow such sequence. A queue can
be implemented using doubled linked listed for example. An array is also an 
option.
- Running time:
    - `O(m+n)`, linear time.
- Use cases:
    - Can compute shortest paths.
    - Can find connected components of undirected graphs.

### DFS (Depth Fisrt Search)

- Explore layer after layer (depth) aggressively, only backtrack when necessary.
- The graph is traverse in a LIFO sequence (Last In First Out): vertices are 
explored in depth, as opposed to depth (BFS).
- The stack is the natural data structure to follow such sequence. A stack can
be easily represented by an array.
- Running time: 
    - `O(m+n)`, linear time.
- Use cases:
    - Compute a topological ordering of a directed acyclic graph.
    - Finds strongly connected components of directed graphs.

## Misc

### HackerRank
I am solving problems from HackerRank. Right now mostly focused on the interview ooriented challenges. Will be documenting more aspects of the these challenges in the future.

#### Search
Several problems solved involving binary search and other search techniques. Sometimes, they require hash maps and sets to make the algorithm more efficient.
    
### Hangman

### Card deck 


