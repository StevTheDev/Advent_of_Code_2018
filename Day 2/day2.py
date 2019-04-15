import os, csv

def check(string):
    ''' Parse a string and return a tuple of boolean int values:
        two if any character appears exactly 2 times in the string
        three if any character appears exactly 3 times in the string
    '''
    seen = {} 
    for char in list(string):
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] = seen[char] + 1
    two = three = 0
    for char in seen:
        if two and three:
            break
        elif seen[char] == 2:
            two = 1
        elif seen[char] == 3:
            three = 1
    return (two, three)

# Read Input
input_path = os.path.join(os.getcwd(),'input.txt')
boxIDs = [line for line in open(input_path).readlines()]

# Calculate Sums with check()
sum_two = sum_three = 0
for boxID in boxIDs:
    count_two, count_three = check(boxID)
    sum_two += count_two
    sum_three += count_three

# Calculate Checksum (Part 1)
checksum = sum_two * sum_three
print(checksum) # Part 1 Answer

# Find boxIDs which vary by only 1 character
count_differences = 0
for boxID in boxIDs:
    if count_differences == 1:
        break
    for comparison in boxIDs:
        if boxID != comparison:
            count_differences = 0
            for a,b in zip(boxID,comparison):
                if a != b:
                    count_differences += 1

            if count_differences == 1:
                # Make string out of duplicate characters
                output = ''.join([char for i, char in enumerate(boxID) if boxID[i] == comparison[i]])
                print(output) # Part 2 Answer
                break
