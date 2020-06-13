#find minimum is sorted and rotated array
class c:
    c = 0
    def __init__(self, i):
        self.c = self.c + i

conditions = c(0)

def findminimum(array, start, end):
    #print(start, end)

    #note down number of conditions
    conditions.c = conditions.c + 1

    #first thing first, check argument validity
    if array is None:
        return -1
    if start == end:
        return start

    #if in sorted array, left element is smaller than right element
    if array[start] < array[end]:
        return start

    mid = int((end+start)/2)

    if array[mid] > array[mid+1]:
        return mid+1

    if array[start] < array[mid]:
        return findminimum(array, mid+1, end)
    elif array[start] > array[end]:
        return findminimum(array, start, mid)
    print("residuals")

array = [25, 16, 17, 18, 19, 20, 21, 22, 23, 24]
#array = [1]
#array = [None]
min = findminimum(array, 0, len(array)-1)
print("Array length:",len(array)-1)
print("Conditions checked:", conditions.c)
print("Minimum number index is:", min)
