def dieHard(h,a):
    count = 0
    current = 0 # Trạng thái ban đầu đang là fire or water
    while(1):
        if current == 0: # gọi đến air
            current = 1
            a+=2
            h+=3
            count+=1
        if current == 1: # gọi đến fire or water        
            if h - 5 > 0 and a - 10 > 0: # check fire
                current = 0
                h-=5
                a-=10
                count+=1
            elif h - 20 > 0 and a +5 > 0: # check water
                current = 0
                h-=20
                a+=5
                count+=1
            else: # Nếu cả 2 đều đie thì thoát
                break
    return count

print(dieHard(1000,1000))
