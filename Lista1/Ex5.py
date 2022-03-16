def is_palindrome(str):
    for i in range(len(str)//2):
        if(str[i] != str[-1-i]): #checks if pairs of letters match
            return False
    return True