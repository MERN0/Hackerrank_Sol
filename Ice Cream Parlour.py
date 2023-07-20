'''Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.'''


def icecreamParlor(m, arr):
    # Write your code here
    res=[]
    n=len(arr)
    for i in range(n-1, -1, -1):
        if i<m:
            for j in range(i):
                if arr[i] + arr[j] == m:
                    res = [j+1, i+1]
    return res
