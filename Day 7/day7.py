import os, re

problem_input = []

input_path = os.path.join(os.getcwd(),'7','input.txt')
for i, line in enumerate(open(input_path).read().split('\n')):
    data = re.findall(r' \w ',line)
    try:
        # data[1] contains a step; data[0] contains the step's dependency
        problem_input.append((data[1][1:2],data[0][1:2]))
    except IndexError:
        print(f'No pattern matches on line {i}: "{line}"')

step_dependencies = {}
for step, dependency in problem_input:
    if step not in step_dependencies:
        step_dependencies[step] = set()

    if dependency not in step_dependencies:
        # Catches steps which do not appear first in input
        step_dependencies[dependency] = set()

    step_dependencies[step].add(dependency)

completed_steps = []
while len(completed_steps) < len(step_dependencies):
    
    available_steps = []
    for step in step_dependencies:
        if step not in completed_steps:
            if step_dependencies[step].issubset(set(completed_steps)):
                available_steps.append(step)

    for step in sorted(available_steps):
        completed_steps.append(step)
        break

print('Step completion order:')
print(''.join(completed_steps))

# Using ord() to get the ASCII value of a character
# such that (ord('A') - 64) = 1
step_time_requirements = { step: 60 + (ord(step) - 64) for step in step_dependencies}

num_workers = 5
workers = { i : '' for i in range(num_workers) }

completed_steps = []
active_steps = {}
time = 0

while len(completed_steps) < len(step_dependencies):
    
    # Find Current Available Steps
    available_steps = []
    for step in step_dependencies:
        if not step in completed_steps and not step in active_steps:
            if step_dependencies[step].issubset(set(completed_steps)):
                available_steps.append(step)
    
    # Assign Available Steps if possible
    for step in sorted(available_steps):
        for worker in workers:
            if workers[worker] == '':
                workers[worker] = step
                active_steps[step] = step_time_requirements[step]
                available_steps.remove(step)
                break   

    # Advance Time
    time += 1
                
    # Update Active Steps
    finished_steps = []
    for step in active_steps:
        active_steps[step] = active_steps[step] - 1
        if active_steps[step] == 0:
            completed_steps.append(step)
            finished_steps.append(step)
            
            for worker in workers:
                if workers[worker] == step:
                    workers[worker] = ''
                    
    # Remove finished_steps from active_steps
    for step in finished_steps:
        del active_steps[step]

print('New completion order:')
print(''.join(completed_steps))
print(f'Step completion will take {time} seconds.')
