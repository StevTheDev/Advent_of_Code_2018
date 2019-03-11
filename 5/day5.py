import os   

def quick_trim(string,keys=()): # Kudos /u/andrewrmg for the inspiration!
    result = ['']
    for char in string:
        if char not in keys:
            last = result[-1]
            if last != char and last.lower() == char.lower():
                # char is of unstable opposite polarity. Examples:        
                #  'a' != 'A' and lower('a') == lower('A')
                #  'A' != 'a' and lower('A') == lower('a'):
                result.pop(-1)
            else:
                # char is a stable sequence addition
                result.append(char)

    result.pop(0)
    return result

# Begin
data = open(os.path.join(os.getcwd(),'5','input')).read().strip()

# Part 1:
length = len(quick_trim(data))
print(f'Reduction Complete. Resulting Polymer Length:{length}')

# Part 2:
shortest = len(data) # Start at Maximum length. Then reduce based on results 
shortest_keys = () # Record the Keys which when purged give the shortest result

for key in range(65,91): # A - Z Uppercase Ascii
    keys = (chr(key),chr(key+32))
    length = len(quick_trim(data,keys))

    if length < shortest:
        shortest = length
        shortest_keys = keys

print(f'Purge {shortest_keys[0]}/{shortest_keys[1]} 
        for Minimum Resulting Polymer Length: {shortest}')