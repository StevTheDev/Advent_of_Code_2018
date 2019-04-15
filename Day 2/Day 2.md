# [**Day 2:** *Inventory Management System*](https://adventofcode.com/2018/day/2)

Part one of this problem requires us to process a list of strings in order to calculate a checksum value. The checksum is the multiplication result of two counts. The characters in each string are counted, and if a character appears exactly two or three times, one or the other of the counters is incremented. 

Part two requires finding a pair of strings which differ by only a single character. In turn each string is compared, character by character, with every other string. Any differences will increment a counter, which if equal to 1 at the end of the string comparision will break the loop. The answer is a string built out of the characters each string had in common.