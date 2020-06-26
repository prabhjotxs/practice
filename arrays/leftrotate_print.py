def leftrotate_print(array, end, k):
    for i in range(0, end):
        n = (k+i)%(end)
        print(array[n], end=" ")

array = [1, 3, 5, 7, 9]
len = len(array)
k = 3
n = k%len
leftrotate_print(array, len, n)
