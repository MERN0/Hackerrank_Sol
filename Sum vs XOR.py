'''Given an integer , find each  such that:
where  denotes the bitwise XOR operator. Return the number of 's satisfying the criteria.'''


def sumXor(n):
    # Write your code here
    res=1
    while n:
        b = n&1
        n >>= 1
        if b==0:
            res = res*2
            
    return res
