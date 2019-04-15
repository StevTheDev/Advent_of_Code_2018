# [**Day 1:** *Chronal Calibration*](https://adventofcode.com/2018/day/1)

Part one is solved by finding the sum of a given list of *n* signed integers.

Part two is solved by repeatedly looping through the list, keeping track of each resulting frequency. By using the python Set object we can check if the result of the frequency adjustment has already been seen in just O(1) time. Once a frequency is encountered twice the loop exits and the answer is printed.