'''There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.'''


def sockMerchant(n, ar):
    # Write your code here
    dic = {}
    c=0
    
    for i in ar:
        dic[i] = dic.get(i, 0) + 1
        
    for i in dic.keys():
        c += dic[i]//2
        
    return c
