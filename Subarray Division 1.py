'''Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.'''

def birthday(s, d, m):
    # Write your code here
    c=0
    totalSum = sum(s[:m])
    
    if totalSum == d:
        c+=1

  #  sliding window
    for i in range(m, len(s)):
        totalSum += s[i] - s[i-m]
        
        if totalSum == d:
            c+=1
            
    return c
