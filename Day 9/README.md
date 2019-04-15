# [**Day 9:** *Marble Mania*](https://adventofcode.com/2018/day/9)

By using a `deque` to store the marble circle the `rotate` method allows us to keep the "current marble" at the front of the deque. This allows it to be read faster than an arbitrary list lookup. `rotate` can also be used to position the deque before quickly appending new elements to the front of the deque. In this problem the distance being rotated is small and predictable and so `rotate` linear time.

By building the list of available marbles out of the *reversed* `range(num_marbles)` the lowest numbered marble can be retreived with pop() very quickly.