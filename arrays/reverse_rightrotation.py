def reverse(array, start, end):
    while (start < end):
        array[start], array[end] = array[end], array[start]
        start = start + 1
        end = end - 1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
len = len(array)
k = 3
reverse(array, 0, len-1)
reverse(array, 0, k-1)
reverse(array, k, len-1)
print(array)
