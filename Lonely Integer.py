'''Given an array of integers, where all elements but one occur twice, find the unique element.'''
#XOR returns the non repeated integer

def lonelyinteger(a):
    # Write your code here
    res=0
    
    for i in a:
        res ^= i
    return res
