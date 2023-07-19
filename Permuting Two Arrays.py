'''There are two -element arrays of integers, A and B. Permute them into some A' and B' such that the relation A'[i]+B'[i]>=k holds for i.'''

def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return 'NO'
    
    return 'YES'
