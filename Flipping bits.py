'''You will be given a list of 32 bit unsigned integers. Flip all the bits (0 to 1 and 1 to 0) and return the result as an unsigned integer.'''

def flippingBits(n):
    # Write your code here
    res = (2**32) + ~n
        
    return res
