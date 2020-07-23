arr = [10, 8, 6, 12, 4, 14, 13, 17, 8, 3, 1]
def mergeSort(arr, l, r):
    i = j = k = 0
    print(arr)
    if (len(arr) > 1):
        mid = (len(arr)+1)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left, 0, mid)
        mergeSort(right, mid, r)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

mergeSort(arr, 0, len(arr))
print(arr)
