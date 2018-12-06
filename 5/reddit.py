from string import *
import os

# Solution from /u/andrewrmg on reddit - Very quick!
# https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4jzni/

def collapse(s):
    p = ['.']
    for u in s:
        v = p[-1]
        if v != u and v.lower() == u.lower():
            p.pop()
        else:
            p.append(u)
    return len(p) - 1


s = open(os.path.join(os.getcwd(),'5','input')).read().strip()
print(collapse(s))
#print(min(collapse(c for c in s if c.lower() != x) for x in ascii_lowercase))