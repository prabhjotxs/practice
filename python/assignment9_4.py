#fname = input("Enter file name: ")
fh = open("files/mbox-short.txt")

email = dict()
largest_till_now_count = 0
largest_till_now_key = 0

for line in fh:
    if not line.startswith('From '): continue
    words = line.split()
    email[words[1]] = email.get(words[1], 0) + 1
    if email[key] > largest_till_now_count:
        largest_till_now_key = words[1]
        largest_till_now_count = email[words[1]]

print(largest_till_now_key, email[largest_till_now_key])