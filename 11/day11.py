def make_point_field(serial_no = 8868):
    point_field = []
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

        point_field.append(row)
    return point_field

def max_sum_subarray(A, subarray_size = 3):
    
    overall_max = test_max = 0
    max_subarray_start = max_subarray_end = 0
    test_subarray_start = test_subarray_end = 0
    
    overflow_protect = False
    for i in range(len(A)):
        test_max = 0
        test_subarray_start = i
        test_subarray_end = test_subarray_start + subarray_size
        for j in range(subarray_size):
            try:
                test_max += A[i+j]
            except IndexError:
                overflow_protect = True
                break

        if overflow_protect:
            break

        if test_max > overall_max:
            overall_max = test_max
            max_subarray_start, max_subarray_end = test_subarray_start, test_subarray_end
            
    return overall_max, max_subarray_start, max_subarray_end

def make_summed_area_table(point_field):
    rows = len(point_field)
    cols = len(point_field[0])
    table = [[0 for c in range(cols)] for r in range(rows)]
    #st[x,y] = pf[x,y] + st[x,y-1] + st[x-1,y] - st[x-1,y-1]
    print(rows,cols)
    for y in range(rows):
        for x in range(cols):
            A = point_field[y][x]
            try:
                B = table[y - 1][x] # if in bounds else 0
            except IndexError:
                B = 0
            try:
                C = table[y][x - 1] # if in bounds else 0
            except IndexError:
                C = 0
            try:
                if x == 0:
                    D = table[y-1][x]  
                else:
                    D = table[y-1][x-1] # if in bounds else 0
            except IndexError:
                D = 0

            table[y][x] = A + B + C - D

    return table
    
def query_summed_area_table(table,x,y,size=3):
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
    
    result = D + A - (B +C)
    return result

point_field = make_point_field(42)
table = make_summed_area_table(point_field)
print(query_summed_area_table(table,20,60))