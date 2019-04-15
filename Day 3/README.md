# [**Day 3:** *No Matter How You Slice It*](https://adventofcode.com/2018/day/3)

**Part 1** of this problem requires processing a list of points and dimensions, then determine the total area overlapped by at least two of the defined regions. The input is parsed into useable integers and a python dictionary structure is used to remember which points have been overlapped by simulating a 2-D array.

**Part 2** then asks to identify which claim is not overlapped by any other claim. By comparing the claims against the matrix assembled in part 1, it's easy to determine when a safe claim is found.