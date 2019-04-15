import os, re, math

def plot_points(points):
    x = sorted([point[0] for point in points])
    y = sorted([point[1] for point in points])
    min_x, max_x = x[0], x[-1]
    min_y, max_y = y[0], y[-1]

    plot = {}
    plot['coords'] = {}
    plot['x_bounds'] = (min_x,max_x)
    plot['y_bounds'] = (min_y,max_y)

    for y in range(min_y, max_y+1):
        if y not in plot['coords']:
            plot['coords'][y] = {}
        
        for x in range(min_x, max_x+1):
            if x not in plot['coords'][y]:
                plot['coords'][y][x] = {}
    return plot

def get_closest_given_point(point,given_points):
    x,y = point
    closest_point = '.'
    min_distance = math.inf
    
    if (x,y) in given_points:
        return given_points[point]['id']
    
    for gp in given_points:
        distance = abs(gp[0] - x) + abs(gp[1] - y)
        if distance == min_distance:
            closest_point = '!'
        elif distance < min_distance:
            closest_point = given_points[gp]['id']
            min_distance = distance
    return closest_point

# /////////////////////////////////////////////////////////////////////
threshold = 10000
input_path = os.path.join(os.getcwd(),'6','input.txt')
input_data = open(input_path).readlines()

given_points = {}
for i,line in enumerate(input_data):
    try:
        x,y = re.findall(r'-?\d+',line)
        point = (int(x),int(y))
        tag = chr(i+65) if i < 26 else chr(i+71)
        given_points[point] = {}
        given_points[point]['id'] = tag
    except ValueError:
        print(f'No pattern matches found on line {i}: {line}')
                                                
fininte_regions = {given_points[point]['id'] : 0 for point in given_points}
safe_area = 0 

plot = plot_points(given_points)
y_bounds = plot['y_bounds']
x_bounds = plot['x_bounds']

for y in range(y_bounds[0],y_bounds[1]+1):
    for x in plot['coords'][y]:
        region_id = get_closest_given_point((x,y),given_points)
        plot['coords'][y][x]['Region'] = region_id

        if region_id in fininte_regions:
            if x in x_bounds or y in y_bounds:
                del fininte_regions[region_id]
            else:
                fininte_regions[region_id] += 1

        distance_sum = 0
        for loc in given_points:
            loc_x, loc_y = loc
            distance_sum += abs(loc_x - x) + abs(loc_y - y)
        if distance_sum < threshold:
            safe_area += 1

isolated_region = max(fininte_regions, key=lambda x: fininte_regions[x])
max_area = (isolated_region, fininte_regions[isolated_region])

print(f'AoC Answer Part 1:')
print(f'Location {max_area[0]} had the largest area: {max_area[1]}')

print(f'AoC Answer Part 2:')
print(
    f'The region containing all locations which have a total distance to '
    f'all given coordinates of less than 10000 has an area of {safe_area}.'
)
