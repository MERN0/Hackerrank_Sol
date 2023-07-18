'''Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.'''

def timeConversion(s):
    # Write your code here
    hrs=int(s[0:2])
    mins=int(s[3:5])
    secs=int(s[6:8])
    half=s[8:]
    
    if half=='PM' and hrs<12:
        hrs=hrs+12
        
    elif half=='AM':
        if hrs==12:
            hrs=0
            
    res = (str(hrs)).zfill(2) + ':' + (str(mins)).zfill(2) + ':' + (str(secs)).zfill(2)
    return res
