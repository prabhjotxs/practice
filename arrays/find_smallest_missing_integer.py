def findMissing(array, l):
    for i in range(0, l):
        j = abs(array[i]) - 1
        if j < l:
            if (array[j] > 0):
                array[j] = -array[j]

    for i in range(0, l):
        if (array[i] > 0):
            return i+1
    return l+1

def shiftNegative(array, l):
    a = 0
    for i in range(l):
        if array[i] < 1:
            array[a], array[i] = array[i], array[a]
            a = a + 1
    return a


array = [2, -3, 3, 4, -5, 1, 5, 6, 7, 8, 9]
l = len(array)
start = shiftNegative(array, l)
element = findMissing(array[start:], l-start)
print("the smallest positive integer missing is:", element)
