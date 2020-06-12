fh = open('files/mbox-short.txt')

ntimes = {}

for line in fh:
    if line.startswith('From '):
        pieces = line.split()
        time_pieces = pieces[5].split(':')
        ntimes[time_pieces[0]] = ntimes.get(time_pieces[0], 0) + 1

for (key, value) in sorted(ntimes.items()):
    print(key, value)