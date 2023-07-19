'''Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.'''


def pageCount(n, p):
    # Write your code here
    return min(p//2, n//2 - p//2)
