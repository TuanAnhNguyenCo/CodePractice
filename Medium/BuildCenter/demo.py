import time
def sortBySalary(a):
    return a[3]

def check(a,b):
    c = a- b
    if c < 0:
        return -1
    return c
def Calendar(hire,staff):
    money = 0
    for i in hire:
        for j in range(i[0],i[1]+1):
                if staff[j-1] > 0:
                    if  staff[j-1] >= i[2]:
                        money += i[2]*i[3]
                        staff[j-1] -=i[2]
                    else:
                        money += staff[j-1]*i[3]
                        staff[j-1] = 0  
        if max(staff) == 0:
            break
          
    return money
def building(hire,n,k):
    hire = sorted(hire,key = sortBySalary)
    staff = [k for i in range(0,n)]

    money = Calendar(hire,staff)
    
    return money

hire = [[2,5,3,1],[1,4,5,3],[1,1,5,1],[3,4,5,6]]
print(building(hire,5,5))
