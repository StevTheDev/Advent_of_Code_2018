import os


def reduce(polymer):

    reduced = False
    while not reduced:
        reduction = []
        reduced = True
        last = 0

        for i in range(len(polymer)):

            if polymer[i] == '!':
                continue

            try:
                char = polymer[i]
                ascii_char = ord(char)
            except:
                ascii_char = None

            try:
                peek = polymer[i+1]
                ascii_peek = ord(peek)
            except:
                ascii_peek = None
                reduction = reduction + polymer[last:i+1]

            if ascii_char and ascii_peek:
                #if peek != (char+32) and peek != (char-32):
                #    reduction = reduction + [polymer[i]]
                #else:
                if ascii_peek == (ascii_char+32) or ascii_peek == (ascii_char-32):
                    reduced = False

                    reduction = reduction + polymer[last:i]
                    last = i+2
                    polymer[i] = polymer[i+1] = '!'


        polymer = reduction
        

    return polymer                              
            
        
            


data = open(os.path.join(os.getcwd(),'5','input')).read().strip()


polymer = []
for char in data:
    polymer.append(char)

reduction = reduce(polymer)
print(f'Reduction Complete. Resulting Polymer Length:{len(reduction)}')