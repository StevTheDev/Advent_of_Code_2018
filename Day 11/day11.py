def make_power_grid(serial_no = 8868):
    power_grid = []
    for y in range(1,301):
        row = []
        for x in range(1,301):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += serial_no
            power_level *= rack_id

            if abs(power_level) < 100:
                power_level = 0
            else:
                power_level = ((power_level % 1000) - (power_level % 100)) / 100

            power_level -= 5
            row.append(power_level)

        power_grid.append(row)
    return power_grid

def make_summed_area_table(points):
    '''
        Implementation of
        https://en.wikipedia.org/wiki/Summed-area_table
    '''
    rows = len(points)
    cols = len(points[0])
    table = [[0 for c in range(cols)] for r in range(rows)]
    #table[y][x] = points[y][x] + table[y-1][x] + table[y][x-1] - table[y-1][x-1]
    for y in range(rows):
        for x in range(cols):
            A = points[y][x]
            try:
                B = table[y - 1][x]
            except IndexError:
                B = 0
            try:
                C = table[y][x - 1]
            except IndexError:
                C = 0
            try:
                if x == 0:
                    D = table[y-1][x]  
                else:
                    D = table[y-1][x-1]
            except IndexError:
                D = 0
            table[y][x] = A + B + C - D
    return table

def query_summed_area_table(points,table,x,y,size=3):
    if x == 0 or y == 0:
        result = 0
        for row in range(y,y+size):
            for col in range(x,x+size):
                result += points[row][col]
        return result
    
    size -= 1 # Minus 1 to accomidate 0 index
    try:
        A = table[y-1][x-1]
    except IndexError:
        A = 0
    try:
        B = table[y-1][x+size]
    except IndexError: 
        B = 0
    try:
        C = table[y+size][x-1]
    except IndexError: 
        C = 0
    try:
        D = table[y+size][x+size]
    except IndexError: 
        D = 0
    
    result = A + D - (B + C)
    return result

def find_max_grouping(points,table,size=3):
    max_result = max_x = max_y = 0
    field_size = (len(points),len(points[0]))

    for row in range(field_size[0]- (size-1)):
        for col in range(field_size[1]- (size-1)):
            try:
                value = query_summed_area_table(points,table,col,row,size)
                if value > max_result:
                    max_result = value
                    max_x = col
                    max_y = row
            except IndexError:
                print(f'Index Error Row {row} Col {col}')
    return max_result,max_x+1,max_y+1

power_grid = make_power_grid()
table = make_summed_area_table(power_grid)
print(find_max_grouping(power_grid,table))

max_result = max_x = max_y = size = 0
for i in range(3,15):
    result,x,y = find_max_grouping(power_grid,table,i)
    if abs(result) > max_result:
        max_result,max_x,max_y,size = result,x,y,i

print(max_x,max_y,size)
