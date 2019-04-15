# [**Day 5:** *Alchemical Reduction*](https://adventofcode.com/2018/day/5)

This problem requires iterating through a long string input which is being shortened according to some given rules. Once eliminating characters, my original solution would skip any resulting rule matches and required multiple iterations of the string. However kudos to */u/andrewmg* for sharing their method of implementation. This method, which I've implemented here, cleverly operates a list object like a stack and can completely reduce the input in one pass.

Noteable advantages of this approach include:

* Constrained Iteration Limit
* Reduced Memory Overhead

The algorithm takes advantage of python's list `append()` and `pop()` methods to efficiently build a `result` string while iterating through the `input`. 

* For each character in `input`:
  * if the last character of `result` paired with the `input` character would trigger reduction, call `pop()` on `result` and move on to the next character in `input`. 
  * Otherwise `append` the `input` character to `result` and move on to the next character in `input`.

**Part 2** requires modification of the algorithm to allow specific characters to be blacklisted from `result`.
