#Quickly find multiple left rotations of an array
def rotate(arr, ntimes):
    ntimes = ntimes%len
    for i in range(ntimes, ntimes+len):
        print(temp_arr[i], end = " ")

arr = [3, 5, 7, 9, 11, 13]
len = len(arr)

temp_arr = [None] *(2*len)
for i in range(0, len):
    temp_arr[i] = temp_arr[i+len] = arr[i]

k = 2
#rotate(temp_arr, k)

k = 6
#rotate(temp_arr, k)

k = 8
rotate(temp_arr, k)
