'''A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. 
Ignore case. Return either pangram or not pangram as appropriate.'''

def pangrams(s):
    # Write your code here
    res = set(s.lower()) - set(' ')
    
    if len(res)==26:
        return 'pangram'
    else:
        return 'not pangram'
