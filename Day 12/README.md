# [**Day 12:** *Subterranean Sustainability*](https://adventofcode.com/2018/day/12)

By giving each pot an id and storing their status in a dictionary object, the contents of each pot can quickly be checked. A string assembled out of a group of pot's contents can be compared against a dictionary of rule strings to determine what state the center pot will have in the next generation. By storing the pots in a dictionary instead of a list, more are quickly added without compromising access time.
