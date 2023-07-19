'''Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. 
If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.'''


def caesarCipher(s, k):
    # Write your code here
    res=''
    for char in s:
        if char.isalpha():
            if char.isupper():
                res += chr((ord(char) - 65 + k)%26 + 65)
            else:
                res += chr((ord(char) - 97 + k)%26 + 97)
        else:
             res += char   
    return res
