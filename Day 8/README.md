# [**Day 8:** *Memory Maneuver*](https://adventofcode.com/2018/day/8)

This problem requires implementing a tree structure then populating and analyzing it with recursive methods.  

The input for this problem is a list of numbers which define the elements in the tree. Specifically the input consists of this sequence:

1. A header, which is always exactly two numbers:
    * The quantity of child nodes.
    * The quantity of metadata entries.

2. Zero or more child nodes (as specified in the header).
3. One or more metadata entries (as specified in the header).

Each child node is then itself a node that has its own header, child nodes, and metadata. 

The first node's meta data appears at the end of the file after all of the children nodes and their metadata. Since the exact starting position of the metadat is unknown, the children nodes must be processed first. This can be achieved with a recursive function, which calls itself to read a node's children nodes, then the node's metadata.

Given the known sequence and structure of the input, the recursive function can pop elements from the front of the list according to initial quantities it reads. By converting the list into a deque collection, elements can be popped off the front of the deque much faster than if it remained a list. *kudos to [/u/johnathan_paulson](https://reddit.com/u/johnathan_paulson).*

Analyzing the tree can then be done recursivly.  

For **Part 1** the metadata for each child is summed and totled, to which the current node's metadata sum is added and returned.

For **Part 2** the subtotal is calculated differently - according to some rules defined in the problem.