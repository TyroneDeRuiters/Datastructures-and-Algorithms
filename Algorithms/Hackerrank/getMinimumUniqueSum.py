def getMinimumUniqueSum(arr):
    stack = list()
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        if(len(stack) == 0):
            stack.append(arr[i])
        else:
            top = stack[len(stack) - 1]
            if(top > arr[i]):
                arr[i] = top
            if(top == arr[i]):
                arr[i] += 1
            stack.append(arr[i])
    print(stack)
    return sum(stack)

print(getMinimumUniqueSum([1,2,2]))
