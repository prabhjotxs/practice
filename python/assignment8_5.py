#fname = input("Enter file name: ")
fh = open("files/mbox-short.txt")
lst = list()
for line in fh:
    if not line.startswith("From:"): continue
    words = line.split()
    #if words[1] not in lst:
    lst.append(words[1])
    print(words[1])

count = len(lst)
print("There were", count, "lines in the file with From as the first word")
