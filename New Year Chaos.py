'''It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . 
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. 
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.'''


def minimumBribes(q):
    # Write your code here
    bribe = 0
    n = len(q)
    
    for i in range(n-1, -1, -1):
        if q[i] > i+3:
            print('Too chaotic')
            return
        j = max(0, q[i]-2)
        while(i>j):
            if q[i] < q[j]:
                bribe+=1
            j+=1
                
    print(bribe)
