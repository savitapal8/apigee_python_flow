def binarysearch(arr, n, k):
		# code here
    start = 0
    last = n - 1
    mid = 0
    index = -1
    
		
    while start != last:
        n = last - start + 1
        mid = start + int(n/2)

        print("mid: " + str(mid))
        if arr[mid] < k:
            start = mid + 1
            last  = last
        elif arr[mid] > k:
            start = start
            last  = mid - 1
        else:
            index = mid
            break

    if (index == -1 and start == last and arr[start] == k):
        index = start
    print("index: " + str(index))
    return index

arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 14, 16, 19, 22, 23, 25, 26, 27, 29, 31, 34, 35, 36, 38, 39, 40, 45, 46, 48, 50, 51, 52, 57, 59, 60, 61, 63, 67, 68, 69, 71, 75, 76, 77, 79, 81, 82, 83, 86, 87, 88, 90, 92, 93, 94, 95, 96, 98, 99, 100]
binarysearch(arr, 59, 100)