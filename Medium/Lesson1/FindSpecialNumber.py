import math as mt
def isPrime(n): #Kiểm tra số nguyên tố
    n1 = int(mt.sqrt(n))
    for i in range(2,n1+1):
        if n%i==0:
            return False
    return True

def FindPrime(k,x,n,SpecialPrime,odd):
    for i in odd:
        q = x # q này dùng khi mà nó quay lui lại vị trí này và lặp vòng lặp mới thì ta sẽ gán lại x = q
        x = x*10 + i
        if x <= n: # Nếu nhỏ hơn n thì xét tiếp
            if isPrime(x)==True: #Nếu là số Nguyên tố thì sẽ thêm vào list
                SpecialPrime.append(x)
                FindPrime(k+1,x,n,SpecialPrime,odd) # Gọi đệ quy đến thằng tiếp theo
        else: # Nếu mà x > n thì hiển nhiên là các giá trị sau trong mảng odd cũng không thoả mãn 
            break # Nên là sẽ quay lui về thời điểm k = k - 1 
        x = q

def find_special_prime(n):
    odd = [1,3,5,7,9] 
    prime = [2,3,5,7]
    SpecialPrime = []
    for i in prime:
        if i <=n: # Nếu i <= n thì sẽ thêm và gọi đệ quy 
            SpecialPrime.append(i)
            FindPrime(1,i,n,SpecialPrime,odd)
    SpecialPrime.sort() # sắp xếp lại danh sách
    return SpecialPrime

print(find_special_prime(10**7)) # Thời gian chạy: 0.068

""" Ý tưởng: 

- Vì Lần ta bỏ số cuối thì nó cũng phải là số nguyên tố thì mới là số siêu nguyên tố được
- => Số nguyên tố thì là số lẻ không phải số chẵn trừ số 2
- Ý tưởng: Áp dụng quay lui

Chú ý: Số đầu tiên sẽ là số từ bên phải 

- Tạo 1 mảng [2,3,5,7] vì khi ta cắt số cuối thì số đầu tiên mới là số nguyên tố
- Tạo 1 mảng các số lẻ [1,3,5,7,9]
- Mỗi lần chay đệ quy thì ta sẽ thêm 1 số in [1,3,5,7,9] vào bên cạnh số mà đang xét. Kiểm tra nếu là số nguyên tố -> nó là số siêu nguyên tố -> thêm vào mảng specialPrime
- Sau đó lại gọi đệ quy tiếp như trên
- Nếu mà nó chạy hết nó sẽ tự quay lui
"""
