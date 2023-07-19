'''We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .'''


def superDigit(n, k):
    # Write your code here
    def rec(n):
        total=0
        for digit in n:
            total += int(digit)
        total=str(total)
        
        if len(total)==1:
            return total
        else:
            return rec(total)
    
            
    repeated_n = str(rec(n)*k)
    return rec(repeated_n) 
