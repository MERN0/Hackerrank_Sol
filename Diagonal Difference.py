'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.'''

def diagonalDifference(arr):
    # Write your code here
    d1=0
    d2=0
    for i in range (len(arr)):
        d1+=arr[i][i]
        d2+=arr[i][len(arr) -1 - i]
        
    return abs(d1-d2)
