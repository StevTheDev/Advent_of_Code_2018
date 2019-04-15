import os, re
from datetime import datetime, timedelta
from more_itertools import peekable

# Regex used when parsing input
timestamp_regex = r'\[\d\d\d\d-\d\d-\d\d \d\d:\d\d\] '
timestamp_regex = re.compile(timestamp_regex)

event_regex = {
    'guard':r'\d{3,4}', # Guard ID Number
    'sleep':r'falls asleep',
    'wake':r'wakes up',  
}

# Read Input
log = []
input_path = os.path.join(os.getcwd(),'4','input.txt')
for line in open(input_path).readlines():
    timestamp = timestamp_regex.search(line).group()
    timestamp = datetime.strptime(timestamp,'[%Y-%m-%d %H:%M] ')
    # The event text is whatever remains on the line after the timestamp.
    # So by removing the timestamp with '' we are left with the event text. 
    event = re.sub(timestamp_regex,'',line)
    log.append({'timestamp':timestamp,'event':event})

log.sort(key=lambda x:x['timestamp']) # Chronological Sort
log = peekable(log) # more_itertools peekable enables the ability to 
                    # "Look Ahead" while iterating

guards = {} # Keys will be Guard IDs
# The sorted log contains entries in this sequence:
# Guard Begins Shift
# Falls Asleep
# Wakes Up
# ...
# Loop through log and look for this sequence
guard_regex = re.compile(event_regex['guard'])
for entry in log:
    if guard_regex.search(entry['event']):
        # Guard Starts Shift
        guard_id = guard_regex.search(entry['event']).group()
        guard_id = int(guard_id)

        # Record total sleep time with a timedelta object
        # Record the minutes slept on in a dictionary
        sleeptime = timedelta(minutes=0)
        minutes = {}

        peek = log.peek() # Look Ahead then read while event is not guard
        while not guard_regex.search(peek['event']):
            # Read two lines of input assuming they contain a sleep/wake pair.
            # The pattern was verified in the sorted log to support the 
            # assumption. Broken pairs are skipped over if encountered.

            t1 = t2 = None # Zero out the clocks
               
            regex = re.compile(event_regex['sleep'])
            peek = log.peek()
            if regex.search(peek['event']):
                entry = next(log)
                t1 = entry['timestamp']
            
            regex = re.compile(event_regex['wake'])
            peek = log.peek()
            if regex.search(peek['event']):
                entry = next(log)
                t2 = entry['timestamp']
        
            if t1 and t2: # If sleep/wake pair was read successfully 
                sleeptime += (t2 - t1) 

                # Record Minute-to-Minute Statistics  
                start = t1.minute # minute of snoozin
                stop = t2.minute # minute of wakeup

                for minute in range(start,stop): # start to (stop-1) remember
                    minute = minute # To be used as lookup key
                    if minute not in minutes:
                        minutes[minute] = 1
                    else:
                        minutes[minute] += 1
            
            try:
                peek = log.peek()
            except: # End of File
                break # Exit While loop

        # Record Guard Information
        if guard_id not in guards:
            guards[guard_id] = {}
            guards[guard_id]['sleeptime'] = sleeptime
            guards[guard_id]['minutes'] = minutes

        else:
            guard = guards[guard_id]
            
            sleep_counter = guard['sleeptime']
            sleep_counter = sleep_counter + sleeptime
            guard['sleeptime'] = sleep_counter + sleeptime 
            
            for minute in minutes:
                if minute not in guard['minutes']:
                    guard['minutes'][minute] = minutes[minute]
                else:
                    minute_counter = guard['minutes'][minute]
                    guard['minutes'][minute] = minute_counter + minutes[minute]


# Part 1
guard_id = max(guards, key=lambda x: guards[x]['sleeptime'])
guard = guards[guard_id]
minute = max(guard['minutes'], key=lambda x: guard['minutes'][x])
count = guard['minutes'][minute]
best_chance = (guard_id,minute,count) # Doing math with the ints later

# Part 2
second_chance = (0,0,0) # guard id, minute, count
sleeping_record = record_holder = 0
for guard_id in guards:
    guard = guards[guard_id]

    if not guard['minutes']: # This guard never slept
        continue

    minute = max(guard['minutes'], key=lambda x: guard['minutes'][x])
    count = guard['minutes'][minute]
    if count > sleeping_record:
        sleeping_record = count
        record_holder = guard_id
    
    if sleeping_record > second_chance[2]:
        second_chance = (record_holder,minute,sleeping_record)

# Results
print(
    f'Best bet is at 00:{best_chance[1]} while guard #{best_chance[0]} '
    f'is on duty. They were seen snoozing then {best_chance[2]} times.'
)

print(
    f'Second option would be at 00:{second_chance[1]} while '
    f'guard #{second_chance[0]} is on duty. '
    f'They were seen snoozing then {second_chance[2]} times.'
)

# Advent of Code Answer Submissions:
print(f'AoC Answer 1: {best_chance[0] * best_chance[1]}')
print(f'AoC Answer 2: {second_chance[0] * second_chance[1]}')

# Solution By Steven Fitzpatrick stevthedev.com