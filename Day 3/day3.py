import os

'''
Input:
claim,xpos,ypos,width,height

123,3,2,5,4

Coord Representation
 0123456789
0..........
1..........
2...#####..
3...#####..
4...#####..
5...#####..
6..........
7..........
8..........
'''

input_path = os.path.join(os.getcwd(),'input.txt')
lines = open(input_path).readlines()

# Dictionary as 2D Array 
matrix = {}
claims = {}
for i, line in enumerate(lines):
    line = line.replace('#','')
    line = line.replace(' @ ',',')
    line = line.replace(': ',',')
    line = line.replace('x',',')
    
    claim, xpos, ypos, width, height = (int(i) for i in line.split(','))
    if claim not in claims:
        claims[claim] = {
            'xpos' : xpos,
            'ypos' : ypos,
            'width' : width,
            'height' : height,
        }

    # Loop through claim area
    for y in range(ypos,ypos+height):
        if y not in matrix:
            matrix[y] = {}
        for x in range(xpos,xpos+width):
            # Use Coord as Key, Use Value as Overlap Counter
            if x not in matrix[y]:
                matrix[y][x] = 1
            else:
                matrix[y][x] = matrix[y][x] + 1

# Part 1: Total Overlapping Area
overlap = 0
for y in matrix:
    for x in matrix[y]:
        if matrix[y][x] > 1:
            overlap += 1

print(f'Overlap {overlap}') # Answer part 1

# Part 2: Identify "Safe" Claim 
for claim in claims:
    xpos = claims[claim]['xpos']
    ypos = claims[claim]['ypos']
    width = claims[claim]['width']
    height = claims[claim]['height']
    safe = True
    # Loop through claim area

    for y in range(ypos,ypos+height):
        for x in range(xpos,xpos+width):
            # If Overlap Counter > 1 - Not Safe!
            if matrix[y][x] > 1:
                safe = False
                break
    
    if safe:
        print(f'Claim No {claim} is safe') 
        break
else:
    print('No safe Claims were found')
