def helpFind(arr, k):
    arr.sort()
    first = 0
    last = len(arr) - 1
    
    while(first <= last):
        middle = (first + last)//2
        if(arr[middle] == k):
            return 'YES'
        if(arr[middle] < k):
            first = middle + 1
        if(arr[middle] > k):
            last = middle - 1
    return 'NO'

print(helpFind([1,5,4,6,2], 1))
