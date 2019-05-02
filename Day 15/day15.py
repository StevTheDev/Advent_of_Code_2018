import os

class Battleground:

    terrain_sprites = {
        '.':'floor',
        '#':'wall',
    }

    actor_sprites =  {
        'E':'elf',
        'G':'goblin',
    }

    def __init__(self):
        self.grid={}
        self.actors = {}

    def __init__(self, input_file_path):
        if os.path.isfile(input_file_path):
            self.grid = {}
            self.actors = {}

            lines = open(input_file_path).read().split('\n')
            for r, line in enumerate(lines):
                for c, char in enumerate(line):
                    if char in self.terrain_sprites:
                        self.grid[(r,c)] = {
                            'terrain' : self.terrain_sprites[char],
                            'occupied_by' : '',
                        }

                    elif char in self.actor_sprites:
                        n = len(self.actors)
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

    def get_actor_move_order(actors):
        return sorted(self.actors,key=lambda p: players[p]['position'])

    def get_active_actors(actors):
        return [self.actors[a] for a in self.actors if self.actors[a]['status'] != 'dead']

    def get_available_moves(start):
        r,c = start
        adjacent_positions (
            (r+1,c), # North
            (r,c-1), # West
            (r,c+1), # East
            (r-1,c), # South
        )
        available_moves = []
        for pos in adjacent_positions:
            if pos in grid:
                if grid[pos]['terrain'] == 'floor' and not grid[pos]['occupied_by']:
                    available_moves.append(pos)
        return available_moves

    def shortest_path(start,end):
        
        pass

path = os.path.join(os.getcwd(),'Day 15','short.txt')
bg = Battleground(path)

print('done!')