import os, re
from collections import deque

input_path = os.path.join(os.getcwd(),'9','input.txt')

data = open(input_path).read()

expression = re.compile('\d+')
result = expression.findall(data)
num_players, num_marbles = int(result[0]),int(result[1])
num_marbles *= 100
num_marbles += 1 # The input is in points, but there is an extra marble worth 0

scores = [0 for i in range(num_players)]
available = [i for i in reversed(range(num_marbles))]

circle = deque([])
marble = available.pop()
circle.append(marble)

def insert_marble(player):
    marble = available.pop()
    if marble % 23 != 0:
        if len(circle) > 1:
            circle.rotate(-2)
        
        circle.appendleft(marble)
    else:
        scores[player] += marble
        circle.rotate(7)
        scores[player] += circle.popleft()


while len(available) > 0:
    for i in range(num_players):
        if len(available) == 0:
            break
        insert_marble(i)
        # print(f'{i+1}: {circle}')

print('Scores:')
print(f'High Score: {max(scores)}')
#for i in range(num_players):
#    print(f'{i+1}: {scores[i]}')
