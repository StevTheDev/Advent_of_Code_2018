import os

track_chars = ['|','-']
corner_chars = ['\\','/']
intersection_chars = ['+',]
cart_chars = ['^','v','<','>']

num_carts = 0
carts = {}

read_cart_orientation = {
    '^' : 'up',
    'v' : 'down',
    '<' : 'left',
    '>' :'right',
}
show_cart_orientation = {
    'up' : '^',
    'down' : 'v',
    'left' : '<',
    'right' : '>',
    'wrecked' : 'X',
}
cart_grid_replacement = {
    '^' : '|',
    'v' : '|',
    '<' : '-',
    '>' :'-',
}
cart_turn_sequence = ['left','straight','right']

ori_turn_results = {
    'up' : {'left':'left', 'right':'right'},
    'down' : {'left':'right', 'right':'left'},
    'left' : {'left':'down', 'right':'up'},
    'right' : {'left':'up', 'right':'down'},
}

def sorted_carts(carts):
    # Sort Carts by Position to Determine Move Order
    return sorted(carts,key=lambda c : carts[c]['position'])

def active_carts(carts):
# Return a list of all non-wrecked cart id
    return [c for c in carts if carts[c]['orientation'] != 'wrecked']

grid = []
lines = open('input.txt').read().split('\n')
for i, line in enumerate(lines):
    row = []
    for j, char in enumerate(line):
        if char in read_cart_orientation:
            carts[num_carts] = {
                'position': (i,j),
                'orientation': read_cart_orientation[char],
                'sequence': 0,
            }
            num_carts += 1
            char = cart_grid_replacement[char]
        row.append(char)
    grid.append(row)   

def display_grid(grid,carts):
    # If carts is passed, insert their characters, print,
    # then remove their characters again
    replacements = {}
    for c in carts:
        cart = carts[c]
        i,j = cart['position']
        ori = cart['orientation']
        if ori != 'wrecked':
            replacements[c] = grid[i][j]
            grid[i][j] = show_cart_orientation[ori]

    for line in grid:
        print(''.join(line))
    
    for c in carts:
        if c in replacements:
            cart = carts[c]
            i,j = cart['position']
            char = grid[i][j]
            grid[i][j] = replacements[c]
    
num_collisions = 0
collisions = {}
tick = 0
'''
print(f'T = {tick}')
#display_grid(grid,carts)
print('Carts')
for cart in carts:
    print(cart,carts[cart])
print('Collisions')
for collision in collisions:
    print(collision ,collisions[collision])
print(f'--- END T {tick} ---')
'''

while True:
    tick += 1
    for c in sorted_carts(carts):
        cart = carts[c]
        current_pos = cart['position']
        current_ori = cart['orientation']
        current_seq = cart['sequence']
        
        if current_ori == 'wrecked':
            # Skip Wrecked Carts
            continue

        # Lookup Next Position
        if current_ori == 'up':
            next_pos = (current_pos[0]-1,current_pos[1])
            next_char = grid[next_pos[0]][next_pos[1]]

        if current_ori == 'down':
            next_pos = (current_pos[0]+1,current_pos[1])
            next_char = grid[next_pos[0]][next_pos[1]]

        if current_ori == 'left':
            next_pos = (current_pos[0],current_pos[1]-1)
            next_char = grid[next_pos[0]][next_pos[1]]

        if current_ori == 'right':
            next_pos = (current_pos[0],current_pos[1]+1)
            next_char = grid[next_pos[0]][next_pos[1]]

        
        # Detect collisions
        # Wrecked Carts are not considered again
        cart_locations = {carts[i]['position']:i for i in carts if carts[i]['orientation'] != 'wrecked'}
        
        cart['position'] = next_pos
        if next_pos in cart_locations:
            
            collisions[num_collisions] = {
                'tick':tick,
                'position':next_pos,
                'cart_one':c,
                'cart_two':cart_locations[next_pos],
            }
            
            num_collisions += 1
            
            carts[c]['orientation'] = 'wrecked'
            carts[cart_locations[next_pos]]['orientation'] = 'wrecked'
            continue

        
        elif next_char in track_chars:
            # no change in orientation
            continue

        elif next_char in intersection_chars:
            turn_direction = cart_turn_sequence[current_seq]
            if turn_direction == 'straight':
                cart['orientation'] = current_ori
            else:
                turn_result = ori_turn_results[current_ori][turn_direction]
                cart['orientation'] = turn_result

            cart['sequence'] = (cart['sequence'] + 1) % 3
            
        elif next_char in corner_chars:
            # corners[0] ('\\')
            if next_char == corner_chars[0]:
                if current_ori == 'up' or current_ori == 'down':
                    turn_result = ori_turn_results[current_ori]['left']
                    cart['orientation'] = turn_result
                else:
                    turn_result = ori_turn_results[current_ori]['right']
                    cart['orientation'] = turn_result

            # corners[1] ('/')
            if next_char == corner_chars[1]:
                if current_ori == 'up' or current_ori == 'down':
                    turn_result = ori_turn_results[current_ori]['right']
                    cart['orientation'] = turn_result
                else:
                    turn_result = ori_turn_results[current_ori]['left']
                    cart['orientation'] = turn_result
    
    #print(f'T = {tick}')
    #display_grid(grid,carts)
    # print('Carts')
    # for cart in carts:
    #     print(cart,carts[cart])
    #print('Collisions')
    #for collision in collisions:
    #    print(collision ,collisions[collision])
    #print(f'--- END T - {tick} ---')
    
    remaining_carts = active_carts(carts)
    if len(remaining_carts) == 1:
        print('Carts')
        for cart in carts:
            print(cart,carts[cart])
        print('Collisions')
        for collision in collisions:
            print(collision ,collisions[collision])
        c = remaining_carts[0]
        print(f'T{tick} Last Active Cart {c}: {carts[c]}')
        display_grid(grid,carts)
        break
