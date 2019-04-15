# [**Day 4:** *Repose Record*](https://adventofcode.com/2018/day/4)

These problems require analyzing a log file to determine their answers. First, the file is read in and stored as a list of dictionary objects. Each element in the list contains a timestamp and event text corresponding to one entry from the log file. The list is then sorted by the timestamps of it's elements. And finally, the list is parsed and a record of the guards' sleeping patterns is generated.

## **Part 1**

> Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

These metrics can be determined by using python's `max()` function on iterables. By using a lambda function as the `max()` key argument the correct guard and minute are selected.

## **Part 2**

> Of all guards, which guard is most frequently asleep on the same minute?

Each guard's 'minutes' dictionary contains the number of times the guard was asleep at a particular minute. Therefore by looking at each guard's sleeping pattern we can determine the most frequent sleeper.
