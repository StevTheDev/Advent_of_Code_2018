import os, csv

def check(string):
    seen=[]
    count=[]

    for char in list(string):
        if char not in seen:
            seen.append(char)
            count.append(1)
        else:
            count[seen.index(char)] += 1
    two = three = 0
    if 2 in count:
        two = 1
    if 3 in count:
        three = 1
    
    return (two,three)

# Read Input from File
boxIDs = []
with open(os.path.join(os.getcwd(),'input')) as file:
    data = csv.reader(file)
    for row in data:
        boxIDs.append(row[0])

sum2 = sum3 = 0
for boxID in boxIDs:
    result = check(boxID)
    sum2 += result[0]
    sum3 += result[1]
    
checksum = sum2 * sum3
print(checksum)