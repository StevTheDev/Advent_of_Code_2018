import os

# Read Input from File
input_path = os.path.join(os.getcwd(),'input.txt')
adjustments = [int(line) for line in open(input_path).readlines()]

# 1: End Frequency
freq = 0
for number in adjustments:
    freq += number
print(freq) # Answer 1

# 2: First Frequency Seen Twice
freq = 0
seen = set()
duplicates = set()

while not duplicates:
    for number in adjustments:
        freq += number
        if freq in seen:
            if freq not in duplicates:
                duplicates.add(freq)
                print(freq)
                break
        else:
            seen.add(freq)
