import os

def new_generation(generation,rules):
    '''
    Process a generation of pots and 
    '''

    def rule_comparison(string):
            for rule in rules:
                if string == rule:
                    return rules[rule]
            else:
                #print(f'No Match Found! {comparision_string}')
                return generation[i]

    next_gen = {}
    for i in generation:
        comparision_string = ''
        for j in range(i-2,i+3):
            if j not in generation:
                comparision_string = comparision_string + '.'
                next_gen[j] = '.'
            else:
                comparision_string = comparision_string + generation[j]

        next_gen[i] = rule_comparison(comparision_string)
        
    return next_gen

def sum_generation(generation):
    gen_sum = 0
    for i in generation:
        if generation[i] == '#':
            gen_sum += i
    return gen_sum

input_path = os.path.join(os.getcwd(),'12','input.txt')
input_data = open(input_path).read().split('\n') # removes trailing '\n' chars 

initial_state = input_data[0][15:]
initial_size = len(initial_state)

rules = {}
for rule in input_data[2:]:
    # rule is a string like '##### => #'
    rules[rule[:5]] = rule[-1]

generations = []

initial_state = {i:char for i,char in enumerate(initial_state)}
# Pad Initial State with . to simplify algorithm
for i in range(-5,0):
    initial_state[i] = '.'
for i in range(initial_size,initial_size+5):
    initial_state[i] = '.'
    
generations.append(initial_state)

for i in range(21):
    generation = generations[i]
    generations.append(new_generation(generations[i],rules))

print(sum_generation(generations[20]))
