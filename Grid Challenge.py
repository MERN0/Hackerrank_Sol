'''Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not'''


def gridChallenge(grid):
    # Write your code here
    lst = [list(each) for each in grid]
    
    for i in range(len(lst)):
        lst[i].sort()
        
    for i in range (len(lst[0])):
        for j in range(1, len(lst)):
            if not lst[j-1][i] <= lst[j][i]:
                return 'NO'
            
    return 'YES'
