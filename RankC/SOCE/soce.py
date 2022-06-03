import sys

input_ = []
account = {}
times = {}

for i in  sys.stdin:
    n = i
    break

count = 0

for line in sys.stdin:
    count+=1
    input_  = line[0:len(line)-1].split(" ")
    account[input_[0]] = input_[1]
    times[input_[0]] = 0
    if count == int(n):
        break

for i in  sys.stdin:
    k = i
    break
for line in sys.stdin:
    length = len(line)
    count+=1
    if line[length-1] == '\n':
        input_  = line[:length-1].split(" ")
    else:
        input_  = line.split(" ")
    a = account.get(input_[0])
    if a!=None:
        if a == input_[1]:
            times[input_[0]] +=1

for i in times:
    print(times.get(i),end =" ")