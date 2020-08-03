def findNumber(arr, left, right, num):
    if arr is None:
        print("Not found --> arr is None")
        return -1
    if right == 0:
        print("Not found --> right is 0")
        return -1
    if left == right:
        if arr[left] == num:
            print(arr[left])
            print("Found! --> arr[left]")
            return 0
        else:
            print("Not found! --> left == right")
            return -1

    mid = ((right-left))//2
    mid = left+mid

    if mid == 0 and arr[left] == num:
        print(arr[left])
        print("Found!")
        return 0

    #print(left, right, mid, arr[mid], arr[left:right+1])

    if arr[mid] == num:
        print(arr[mid])
        print("Found! --> arr[mid] == num")
        return 0
    elif arr[mid] > num:
        if arr[left] <= num <= arr[mid]:
            return findNumber(arr, left, mid, num)
        else:
            return findNumber(arr, mid+1, right, num)
    elif arr[mid] < num:
        if arr[mid] <= num <= arr[right]:
            return findNumber(arr, mid+1, right, num)
        else:
            return findNumber(arr, left, mid, num)
    else:
        print("need handle")

arr = [10, 11, 12, 14, 16, 18, 2, 4, 6, 8, 9]
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
len = len(arr)

number = 15
print(number)

findNumber(arr, 0, len-1, number)
