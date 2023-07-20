'''Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. 
Given a string , determine if it is valid. If so, return YES, otherwise return NO.'''


from collections import Counter
def isValid(s):
    # Write your code here
    char_counter = Counter(s)
    freq_counter = Counter(char_counter.values())
    
    if len(freq_counter) == 1:
        return 'YES'
    elif len(freq_counter) == 2:
        c1, f1 = freq_counter.popitem()
        c2, f2 = freq_counter.popitem()
        
        if (f2==1 and (c2==1 or c2-c1==1)) or (f1==1 and (c1==1 or c1-c2==1)):
            return 'YES'
    return 'NO'
