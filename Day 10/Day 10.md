# [**Day 10:** *The Stars Align*](https://adventofcode.com/2018/day/10)

Maintaining and tracking the positions of the given points in this problem was pretty straightforward, but I was struggling to understand how to recognize when the solution was reached. So, *kudos to [u/jonathan_paulson](https://www.reddit.com/user/jonathan_paulson) again* for sharing his solution, where each iteration the points are checked against a `max_wdith` constraint. If all the points fall within a range suitable for display on the terminal they are printed. With that constraint in place it's just a matter of iterating until a legible output is produced.