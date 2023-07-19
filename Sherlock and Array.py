'''Watson gives Sherlock an array of integers. 
His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.'''


def balancedSums(arr):
    # Write your code here
    rightTotal = sum(arr)
    leftTotal = 0
    for i in range(len(arr)):
        rightTotal -= arr[i]
        if leftTotal == rightTotal:
            return 'YES'
        leftTotal += arr[i]
    return 'NO'
