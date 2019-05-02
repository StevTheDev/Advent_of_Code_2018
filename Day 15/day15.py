import os, time
from collections import deque

class Battleground:

    terrain_sprites = {
        '.':'floor',
        '#':'wall',
    }

    actor_sprites =  {
        'E':'elf',
        'G':'goblin',
    }

    factions = {
        'good' : ['elf'],
        'evil' : ['goblin'],
    }

    def __init__(self):
        self.grid={}
        self.actors = {}

    def __init__(self, input_file_path):
        if os.path.isfile(input_file_path):
            self.grid = {}
            self.actors = {}

            lines = open(input_file_path).read().split('\n')
            self.grid['height'] = len(lines) -1
            self.grid['width'] = len(lines[0])
            self.grid['size'] = self.grid['height'] * self.grid['width']
            for r, line in enumerate(lines):
                for c, char in enumerate(line):
                    if char in self.terrain_sprites:
                        self.grid[(r,c)] = {
                            'terrain' : self.terrain_sprites[char],
                            'occupied_by' : '',
                        }

                    elif char in self.actor_sprites:
                        n = str(len(self.actors))
                        actor = {
                            'id' : n,
                            'position': (r,c),
                            'class' : self.actor_sprites[char],
                            'hitpoints': 200,
                            'attack': 3,
                            'status': 'waiting',
                        }
                        self.actors[n] = actor
                        self.grid[(r,c)] = {
                            'terrain' : 'floor',
                            'occupied_by' : actor['id'],
                        }

        else:
            raise FileNotFoundError

    def __str__(self):
        actor_sprites = { self.actor_sprites[c] : c for c in self.actor_sprites}
        terrain_sprites = { self.terrain_sprites[c] : c for c in self.terrain_sprites}
        lines = []
        for r in range(self.grid['height']):
            line = []
            for c in range(self.grid['width']):
                pos = (r,c)
                if not self.grid[pos]['occupied_by']:
                    line.append(
                        terrain_sprites[self.grid[pos]['terrain']]
                    )
                else:
                    actor_id = self.grid[pos]['occupied_by']
                    line.append(
                        actor_sprites[self.actors[actor_id]['class']]
                    )

            lines.append(line)

        return '\n'.join(
            [''.join(line) for line in lines]
        )

    def get_actor_move_order(self, actors):
        return sorted(self.actors,key=lambda p: players[p]['position'])

    def get_active_actors(self, actors):
        return [self.actors[a] for a in self.actors if self.actors[a]['status'] != 'dead']

    def get_available_moves(self, start):
        if start not in self.grid:
            raise IndexError

        r,c = start
        adjacent_positions = (
            (r-1, c), # North
            (r, c-1), # West
            (r, c+1), # East
            (r+1, c), # South
        )
        available_moves = []
        for pos in adjacent_positions:
            if pos in self.grid:
                if self.grid[pos]['terrain'] == 'floor' and not self.grid[pos]['occupied_by']:
                    available_moves.append(pos)
        return available_moves

    def shortest_path(self, start, end):
        if start not in self.grid or end not in self.grid:
                raise IndexError

        def breadth_first_search(start, end):
            searched = {}
            search_deque = deque([{
                'position': start,
                'parent_step': 0,
            }])
            search_set = set(start) # a set() is created because there is no
                                    # way to search the deque by position alone
                                    # without extra processing on each loop

            step_id = 0

            while len(search_deque): # while deque is not empty

                # Get next element to search
                search_target = search_deque.popleft()

                position = search_target['position']
                parent_step = search_target['parent_step']

                # Add possible steps to search deque
                available_moves = self.get_available_moves(position)
                for move in available_moves:
                    if move not in searched and move not in search_set:
                        # add move to search deque with parent as current step
                        search_deque.append({
                            'position': move,
                            'parent_step': step_id,
                        })
                        search_set.add(move) 
                
                # Add current step to search deque then remove pos from set
                searched[position] = {
                    'step_id': step_id,
                    'parent': parent_step,
                }
                search_set.discard(position)

                # If the ending position is found, exit the loop
                if position == end:
                    return searched, step_id
                else:
                    step_id += 1

            else: # Deque is empty. No Path Found
                return [], 0
            
        searched, end_step = breadth_first_search(start, end)

        if not searched: # No Path Found
            return []

        # reconstruct path from searched
        searched = { # Restructure searched so step_id is the key. Trade off:
            searched[position]['step_id']: {
                'position': position,
                'parent': searched[position]['parent'] 
            } for position in searched
        } # Cost of len(searched) but allows for fast reconstruction below:
        
        path = []
        step = end_step

        while True:
            path.append(searched[step]['position'])
            parent = searched[step]['parent']
            if step == parent == 0:
                break
            else:
                step = parent

        return list(reversed(path))

path = os.path.join(os.getcwd(),'Day 15','short.txt')
bg = Battleground(path)
print(bg)
start = time.perf_counter_ns()
path = bg.shortest_path((1,27), (29,22))
stop = time.perf_counter_ns()
duration = stop - start
print(f'done in {duration}ns')
print(path)
