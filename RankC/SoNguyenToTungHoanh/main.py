# dung miller rabin
# n-1 = 2^r * d

from random import randint


def CaculateRandD(n):
    n = n-1
    while(n%2==0):
            n = n >> 1
    return n

def MillerRabin(n,k):
    if n == 2: 
        return True
    if n < 2 or n %2==0:
        return False
    if check(n) == False:
        return False
    d = CaculateRandD(n)
    for i in range(k):
        a = randint(2,n-1) # a = [2,n-1]
        c = a**d % n
        temp = d
        while(temp!=n-1 and c !=1 and c!=-1):
            temp  = temp << 1
            c = c**2 % n # <=> a ** temp <=>  a ** d**2

        if c!=n-1 and c!=1:
            return False
    return True

def check(a):
    if a <10:
        return True
    if a%3 ==0:
        return False
    if a%5 ==0:
        return False
    if a%7 == 0: 
        return False
    return True

def Prime(N,string):
    arr = [N]
    result = list(string)
    count = 0
    if N == 2:
        N+=1
    else:
        N+=2
    while(count < 25):
        
        if check(N) and MillerRabin(N,10)==True:
            arr.append(N)
            count+=1
        N+=2
    for i in result:
        print(arr[ord(i)-ord('a')],end = " ")
    print()
import time
start = time.time()
prime = []
for i in range(2,10**6):
    if MillerRabin(i,10) == True:
        prime.append(i)

end = time.time()
print(end-start)
print(prime)







