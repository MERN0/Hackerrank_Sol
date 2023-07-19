'''Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
Declare an integer, , and initialize it to .

There are  types of queries, given as an array of strings for you to parse:

Query: 1 x y
Let .
Append the integer  to .
Query: 2 x y
Let .
Assign the value  to .
Store the new value of  to an answers array.'''


def dynamicArray(n, queries):
    # Write your code here
    arr=[[] for _ in range (n)]
    lastAnswer = 0
    res = []
    
    for q,x,y in queries:
        idx = (x^lastAnswer) % n
        
        if q == 1:
            arr[idx].append(y)
            
        else:
            v= y % len(arr[idx])
            lastAnswer = (arr[idx][v])
            res.append(lastAnswer)
            
    return res
