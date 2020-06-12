import re

fh = open('files/regex_sum_233491.txt')

total = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for number in numbers:
            total = total + int(number)
            
print(total)