import os, csv

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

def parse(row): # Turn input into usable ints
    claim,xpos,ypos,width,height = row
    claim = int(claim)
    xpos = int(xpos)
    ypos = int(ypos)
    width = int(width)
    height = int(height)
    return claim,xpos,ypos,width,height

# Begin
with open(os.path.join(os.getcwd(),'myinput')) as file:
    data = csv.reader(file)

    # Dictionary as 2D Array 
    matrix = {}
    
    # Read input
    for row in data:
        claim,xpos,ypos,width,height = parse(row)

        # Loop through claim area
        for x in range(xpos,xpos+width):
            for y in range(ypos,ypos+height):
                # Use Coord as Key, Use Value as Overlap Counter
                if f'({x},{y})' not in matrix:
                    matrix[f'({x},{y})'] = 1
                else:
                    matrix[f'({x},{y})'] += 1

    # Part 1: Overlapping Area
    overlap = 0
    for location in matrix:
        if matrix[location] > 1:
            overlap += 1
    print(f'Overlap {overlap}')

    # Part 2: Safe Area
    file.seek(0) # reset reader
    # Loop Input Again (Counters Must be Complete)
    for row in data:
        claim,xpos,ypos,width,height = parse(row)

        safe = True
        # Loop through claim area
        for x in range(xpos,xpos+width):
            for y in range(ypos,ypos+height):
                # If Overlap Counter > 1 - Not Safe!
                if matrix[f'({x},{y})'] > 1:
                    safe = False
                    break
        
        if safe:
            print(f'Claim No {claim} is safe')
            break