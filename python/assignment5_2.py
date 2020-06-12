largest = None
smallest = None
while True:
    s_num = input("Enter a number: ")
    if s_num == "done" : break
    
    try:
        num = float(s_num)
    except:
        print('Invalid input')
        continue
    
    if (largest is None):
        largest = num
    if (num > largest):
        largest = num
        
    if (smallest is None):
        smallest = num
    if (num < smallest):
        smallest = num
        
    #print(num)
i_largest = int(largest)
i_smallest = int(smallest)
print("Maximum is", i_largest)
print("Minimum is", i_smallest)