# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

content = fh.read()

content_upper = content.upper()
print(content_upper)