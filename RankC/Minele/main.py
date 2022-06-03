input_ = [1,2,3,4,5,6,4,5,4,5,2,5,5,4]
inp = {}
inp1 = {}
max_Idx = {}
for i in range(len(input_)):
    a = inp.get(input_[i])
    if a!=None:
        inp[input_[i]] = i - max_Idx[input_[i]]
        inp1[input_[i]] += 1
        max_Idx[input_[i]] = i
    else:
        inp[input_[i]] = i
        inp1[input_[i]] = 1
        max_Idx[input_[i]] = i


Min = 10**7
for i in inp1:
    if inp1[i] >=2 :
        if Min > inp[i]:
            Min = inp[i]
print(max(inp1.values()))