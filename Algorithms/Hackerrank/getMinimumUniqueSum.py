'''
O(n) solution to get minimum unique sum problem from Hackerrank.com.
'''
def getMinimumUniqueSum(arr):
    arr.sort()
    for i in range(len(arr)):
        if(i == 0):
            prev = arr[i]
        else:
            if(prev > arr[i]):
                arr[i] = prev
            if(prev == arr[i]):
                arr[i] += 1
            prev = arr[i]
    return sum(arr)

print(getMinimumUniqueSum([1,2,2]))
