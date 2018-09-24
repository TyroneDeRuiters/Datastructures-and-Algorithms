'''
memoized algorithm for finding longest increasing then decreasing subsequence
Time complexity: O(n^2)
Space complexity: O(n)
'''

def longestSub(nums, prev, curpos, increase, decreasing, memo):
    if(curpos == len(nums)):
        return 0
    taken = 0
    if(memo[curpos] != None):
        return memo[curpos]
    if(nums[curpos] > nums[prev]):
        if(prev == 0):
            taken = 2 + longestSub(nums, curpos, curpos + 1, True, False, memo)
        else:
            if(decreasing == True):
                return 0
            taken = 1 + longestSub(nums, curpos, curpos + 1, True, False, memo)
    if(nums[curpos] < nums[prev] and (increase or decreasing)):
        taken = 1 + longestSub(nums, curpos, curpos + 1, False, True, memo)
    nottaken = longestSub(nums, curpos, curpos + 1, increase, decreasing, memo)
    memo[curpos] = max(taken, nottaken)
    return memo[curpos]

arr = [1,11,5,3,8]
print(longestSub(arr, 0, 1, False, False, [None] * len(arr)))
