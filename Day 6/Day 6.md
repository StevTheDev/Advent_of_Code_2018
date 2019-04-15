# [**Day 6**: *Chronal Coordinates*](https://adventofcode.com/2018/day/6)

This problem gives a list of (x, y) coordinate and asks for information about cordinates in relation to the given coordinates.

To do so I constructed a coordinate plane containing each given point. Then, looping over each point of the plane:

* The nearest given point is determined.
* Given points are removed from consideration as their regions are determined to be infinite.
* A counter for the closest given point is incremented if the given point's region is finite.
* The cumulative distance from the point to each given point is calculated.
  * If the cumulative distance is within a given theshold, increment a 'safe area' counter

Once this operation is complete:

* **Part 1** can be answered by referencing the maximum finite region counter.
* **Part 2** can be answered by referencing the 'safe area' counter
