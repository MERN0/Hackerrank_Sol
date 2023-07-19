'''Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of . If it is, they divide it by . 
If not, they reduce it by the next lower number which is a power of . Whoever reduces the number to  wins the game. Louise always starts.

Given an initial value, determine who wins the game.'''


def counterGame(n):
    # Write your code here
    bits_one = bin(n-1).count('1')
    
    if bits_one % 2 == 1:
        return 'Louise'
    else:
        return 'Richard'
