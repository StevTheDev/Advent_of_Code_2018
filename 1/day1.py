import os, csv

# Read Input from File
adjustments = []
with open(os.path.join(os.getcwd(),'myinput')) as file:
    data = csv.reader(file)
    for row in data:
        adjustments.append(int(row[0]))

# 1: End Frequency
freq = 0
for number in adjustments:
    freq += number
print(freq) # Answer 1

# 2: First Frequency Seen Twice
freq = 0
seen = []
pairs = []

while not pairs:
    for number in adjustments:
        freq += number
        if freq in seen:
            if freq not in pairs:
                pairs.append(freq)
                break
        else:
            seen.append(freq)

print(pairs[0]) # Answer 2