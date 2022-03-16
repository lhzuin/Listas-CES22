import math
def is_prime(n):
    if(n==1):
        return False
    limit = int(math.sqrt(n)) # 
    prime = True
    for i in range(2,limit+1):
        if(n%i == 0): # if n is divisible by an integer
            prime = False
            break
    return prime