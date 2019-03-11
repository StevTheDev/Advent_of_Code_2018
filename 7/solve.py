import re

problem_input = []
for i, line in enumerate(open('.\\7\\input.txt').read().split('\n')):
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

_ = {}
for k in sorted(step_dependencies, key=lambda k: len(step_dependencies[k])):
    _[k] = sorted(step_dependencies[k])
    
step_dependencies = _


step_time_requirements = { step: 60 + (ord(step) - 65) for step in step_dependencies}

num_workers = 5
workers = { i : '' for i in range(num_workers) }
time = -1

completed_steps = []
active_steps = {}

while len(completed_steps) < len(step_dependencies):
    time += 1

    to_delete = []
    for step in active_steps:
        if active_steps[step] == 0:
            completed_steps.append(step)
            to_delete.append(step)
            
            for worker in workers:
                if workers[worker] == step:
                    workers[worker] = ''
        else:
            active_steps[step] = active_steps[step] - 1
            
    for step in to_delete:
        del active_steps[step]
    
    available_steps = []
    for step in step_dependencies:
        if not step in completed_steps and not step in active_steps:
            if set(step_dependencies[step]).issubset(set(completed_steps)):
                available_steps.append(step)
    
    
    for step in sorted(available_steps):
        if step not in active_steps and step not in completed_steps:
            for worker in workers:
                if workers[worker] == '':
                    workers[worker] = step
                    active_steps[step] = step_time_requirements[step]
                    available_steps.remove(step)
                    break

