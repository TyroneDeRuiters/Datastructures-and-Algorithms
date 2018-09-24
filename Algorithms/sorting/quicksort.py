def quicksort(arr, first, last):
    if(first < last):
        print(arr)
        pi = partition(arr, first, last)
        quicksort(arr, first, pi - 1)
        quicksort(arr, pi + 1, last)

def run():
    arr = [5, 4, 3, 2, 1]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)

def partition(arr,first, last):
    lower = list()
    cnt = first
    while(cnt < last):
        if(arr[cnt] < arr[last]):
            lower.append(arr[cnt])
        cnt += 1
    temp = arr[last]
    arr[last] = arr[first + len(lower)]
    arr[first + len(lower)] = temp
    return first + len(lower)

        
run()
