import os, csv

locations = {}
with open(os.path.join(os.getcwd(),'6','input')) as file:
    file = csv.reader(file)

    for i, row in enumerate(file):
        locations[i] = {}
        #locations[i]['id'] = i
        locations[i]['point'] = (int(row[0]),int(row[1]))
        locations[i]['neighbors'] = {} # ((X,Y),distance)

    

for i in locations:
    place = locations[i]
    point = place['point']
    neighbors = place['neighbors']

    for j in locations:
        neighbor = locations[j]

        if neighbor['point'] != point:

            x1,y1 = point[0],point[1]
            x2,y2 = neighbor['point'][0],neighbor['point'][1]
                        
            distance = abs(x1-x2) + abs(y1-y2)

            counter = (neighbor['point'], distance)

            if counter not in neighbors:
                neighbors[j] = counter



    place['neighbors'] = neighbors


for i in locations:
    place = locations[i]
    print(f"From {place['point']}:")
    for i in place['neighbors']:
        print(f"The distance to {place['neighbors'][i][0]} is {place['neighbors'][i][1]}")

'''
What is the size of the largest area that isn't infinite?

'''

        # (Top Left), (Bottom Right)
bboxbox = ((0,0),(0,0))





finite_areas = {} # ((x,y),area)
for i in locations:
    place = locations[i]
    
    infinite_area = True
    # filter locations:
    x1,y1 = place['point']
    for j in place['neighbors']:
        x2,y2 = place['neighbors'][j][0]
        # if x2 is 'further out' than x1 or y2 is 'further out' than y1:
            infinite_area = False         
            break
    
    if not infinite_area:
        finite_areas
    
