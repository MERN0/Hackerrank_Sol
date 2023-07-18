'''There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings. 
Return an array of the results.'''

def matchingStrings(strings, queries):
    # Write your code here
    counting={}
    
    for string in strings:
        counting[string] = counting.get(string, 0) +1
        
    res = []
    
    for query in queries:
        res.append(counting.get(query, 0))
        
    return res
