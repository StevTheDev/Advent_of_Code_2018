import os, csv, re, itertools
from more_itertools import peekable
from datetime import datetime, timedelta

# Read Input
with open(os.path.join(os.getcwd(),'4','input')) as file:
    data = csv.reader(file)
    
    log = []
    for row in data:
        timestamp_regex = re.compile(r'\[\d\d\d\d-\d\d-\d\d \d\d:\d\d\] ')
        timestamp = timestamp_regex.search(row[0]).group()
        timestamp = datetime.strptime(timestamp,'[%Y-%m-%d %H:%M] ')
        event = re.sub(timestamp_regex,'',row[0])
        #print(f'{timestamp} {event}')
        log.append({'timestamp':timestamp,'event':event})

log.sort(key=lambda x:x['timestamp'])

event_regex = {
    'guard':r'\d{3,4}',
    'sleep':r'falls asleep',
    'wake':r'wakes up',  
}

guards = {}

log = peekable(log)

for entry in log:
    print(f"{entry['timestamp']} {entry['event']}")
    
    guard_regex = re.compile(event_regex['guard'])
    if guard_regex.search(entry['event']):
        guard_id = guard_regex.search(entry['event']).group()

        sleeptime = timedelta(minutes=0)
        minutes = {}

        peek = log.peek()
        while not guard_regex.search(peek['event']): # next line is not guard line

            t1 = t2 = None
            entry = log.next()
            regex = re.compile(event_regex['sleep'])
            if regex.search(entry['event']):
                t1 = entry['timestamp']

            entry = log.next()
            regex = re.compile(event_regex['wake'])
            if regex.search(entry['event']):
                t2 = entry['timestamp']
        
            sleeptime += (t2 - t1) 
            start = t1.minute
            stop = t2.minute

            for minute in range(start,stop):
                print(minute)
                if str(minute) not in minutes:
                    minutes[str(minute)] = 1
                else:
                    minutes[str(minute)] += 1

            print(f'Slept {sleeptime}\t00:{start} - 00:{stop-1}')
            try:
                peek = log.peek()
            except:
                break

        # Exit While
        if guard_id in guards:
            sleep_total = guards[guard_id]['sleeptime']
            sleep_total = sleep_total + sleeptime
            guards[guard_id]['sleeptime'] = sleep_total

            guard_minutes = guards[guard_id]['minutes']
            for minute in minutes:
                if minute in guard_minutes:
                    guard_minutes[minute] = guard_minutes[minute] + minutes[minute]
                else:
                    guard_minutes[minute] = minutes[minute]

            
            #guards[guard_id]['minutes'] = guard_minutes
        else:
            guards[guard_id] = {}
            guards[guard_id]['sleeptime'] = sleeptime
            guards[guard_id]['minutes'] = minutes

print('End!')