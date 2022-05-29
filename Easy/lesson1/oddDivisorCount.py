import math as mt
def solve(a,b):
    count = 0
    for i in range(a,b+1):
        if i == int(mt.sqrt(i))**2: # Kiểm tra xem có phải số chính phương không
            count+=1 # Nếu có thì cộng 1 và số 1 cũng được tính
    return count