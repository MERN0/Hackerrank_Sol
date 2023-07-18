'''Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-1 are acceptable.'''

def plusMinus(arr):
    # Write your code here
    pos= 0
    neg= 0
    zer= 0
    n=len(arr)
    for num in arr:
        if num>0:
            pos+=1
        elif num<0:
            neg+=1
        else:
            zer+=1
            
    print(format(pos/n, '.6f'))
    print(format(neg/n, '.6f'))
    print(format(zer/n, '.6f'))
