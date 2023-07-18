'''Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.'''

def miniMaxSum(arr):
    # Write your code here
    minVal= float('inf')
    maxVal= float('-inf')
    sumVal=0
    for num in arr:
        if num<minVal:
            minVal=num
        if num>maxVal:
            maxVal=num
        sumVal+=num
        
    print(sumVal-maxVal, sumVal-minVal)
