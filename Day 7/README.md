# [**Day 7:** *The Sum of Its Parts*](https://adventofcode.com/2018/day/7)

This problem revolves around determining the proper order in which a set of steps should be completed, given that some steps can only be completed after some others.

Each step's dependencies are stored in a set object, which allows them to quickly be checked against a set of previously completed steps. If the set of a step's dependencies is a subset of the currently completed steps, the step is available to be completed. The list of step dependencies is looped over until the list of completed steps grows to equal length. **Part 1's** answer is the list of completed steps when iteration stops.

For **Part 2** two new dictionary objects are introduces to keep track of which steps are currently being worked on. Available steps are assigned to workers and time is incremented until each step has been completed.