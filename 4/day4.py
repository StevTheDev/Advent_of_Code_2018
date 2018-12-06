import os, csv, re
from datetime import datetime, timedelta
from more_itertools import peekable

# Regex used when parsing input
timestamp_regex = r'\[\d\d\d\d-\d\d-\d\d \d\d:\d\d\] '
event_regex = {
    'guard':r'\d{3,4}', # Guard ID Number
    'sleep':r'falls asleep',
    'wake':r'wakes up',  
}


# Read Input
with open(os.path.join(os.getcwd(),'input')) as file:
    data = csv.reader(file)
    
    log = []
    for row in data:
        timestamp_regex = re.compile(timestamp_regex)
        timestamp = timestamp_regex.search(row[0]).group()
        timestamp = datetime.strptime(timestamp,'[%Y-%m-%d %H:%M] ')

        event = re.sub(timestamp_regex,'',row[0]) # Remove timestamp from string
        
        log.append({'timestamp':timestamp,'event':event})


# Analyze Log and Record Guard Information 
guards = {} # Keys will be Guard IDs
log.sort(key=lambda x:x['timestamp']) # Chronological Sort
log = peekable(log) # So we can look ahead later

for entry in log:

    guard_regex = re.compile(event_regex['guard'])
    if guard_regex.search(entry['event']):
        guard_id = guard_regex.search(entry['event']).group()

        # Record total sleep time with a timedelta object
        # Record the minutes slept on in a dictionary
        sleeptime = timedelta(minutes=0)
        minutes = {}

        peek = log.peek() # Look Ahead then read while event is not guard
        while not guard_regex.search(peek['event']):

            ''' Read two lines of input assuming they contain a sleep/wake pair.
            The pattern was verified in the sorted log to support the assumption
            Broken pairs are skipped over if encountered.
            '''

            t1 = t2 = None # Zero out the clocks
               
            regex = re.compile(event_regex['sleep'])
            peek = log.peek()
            if regex.search(peek['event']):
                entry = log.next()
                t1 = entry['timestamp']
            
            regex = re.compile(event_regex['wake'])
            peek = log.peek()
            if regex.search(peek['event']):
                entry = log.next()
                t2 = entry['timestamp']
        
            if t1 and t2: # If sleep/wake pair was read successfully 
                sleeptime += (t2 - t1) 

                # Record Minute-to-Minute Statistics  
                start = t1.minute # minute of snoozin
                stop = t2.minute # minute of wakeup

                for minute in range(start,stop): # start to (stop-1) remember
                    minute = str(minute) # To be used as lookup key
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
best_chance = (int(guard_id),int(minute),count) # Doing math with the ints later

# Part 2
second_chance = (0,0,0) # guard id, minute, count
for minute in range(60):
    minute = str(minute) # To be used as lookup key

    sleeping_record = 0
    record_holder = 0

    for guard_id in guards:
        guard = guards[guard_id]
        try:
            if guard['minutes'][minute] > sleeping_record:
                sleeping_record = guard['minutes'][minute]
                record_holder = guard_id

        except: # guard['minutes'][minute] does not exist 
            continue # Meaning this guard was never asleep at this time

    if sleeping_record > second_chance[2]:
        second_chance = (int(record_holder),int(minute),sleeping_record)


# Results
print(f'Best bet is at 00:{best_chance[1]} while guard #{best_chance[0]} is on duty. They were seen snoozing then {best_chance[2]} times.')
print(f'Second option would be at 00:{second_chance[1]} while guard #{second_chance[0]} is on duty. They were seen snoozing then {second_chance[2]} times.')

# Advent of Code Answer Submissions:
print(f'AoC Answer 1: {best_chance[0] * best_chance[1]}')
print(f'AoC Answer 2: {second_chance[0] * second_chance[1]}')

# Solution By Steven Fitzpatrick stevthedev.com