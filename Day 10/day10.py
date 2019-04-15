import os, re

input_path = os.path.join(os.getcwd(),'10','input.txt')
input_data = open(input_path).readlines()

expr = r'-?\d+'
expr = re.compile(expr)

points = []

for i, line in enumerate(input_data):
    data = expr.findall(line)
    point = {}
    try:
        point['Position'] = (int(data[0]), int(data[1]))
        point['Velocity'] = (int(data[2]), int(data[3]))
        points.append(point)
    except IndexError:
        print(f'No pattern matches on line {i}: "{line}"')

def update_positions(points):
    for point in points:
        new_x = point['Position'][0] + point['Velocity'][0]
        new_y = point['Position'][1] + point['Velocity'][1]
        point['Position'] = (new_x,new_y)

def plot_points_ascii(points,t):
    max_plot_width = 79
    positions = [point['Position'] for point in points]
    x_list = sorted([position[0] for position in positions])
    y_list = sorted([position[1] for position in positions])
    min_x,max_x = x_list[0],x_list[-1]
    min_y,max_y = y_list[0],y_list[-1]
    if max_x - min_x <= max_plot_width:
        print(f'\nPositions @ t={t}:')
        for y in range(min_y, max_y+1):
            line=''
            for x in range(min_x, max_x+1):
                if (x,y) in positions:
                    line += '#'
                else:
                    line += '.'

            print(line)

plot_points_ascii(points,0)
for t in range(1,11000):
    update_positions(points)
    plot_points_ascii(points,t)
