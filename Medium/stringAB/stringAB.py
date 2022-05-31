results = []
def stringAB(n,k):
    stringAB = ["A","B"]
    strTest = ["." for i in range(0,n)] # Tạo ra 1 list có n phần tử
    GenerateStr(n,0,stringAB,strTest) # Sinh ra các chuỗi AB có độ dài n
   
    return processString(k)
# Hàm sinh ra các chuỗi AB
def GenerateStr(n,m,stringAB,strTest):
    for i in stringAB:
        strTest[m] = i
        if m == n-1: # Nếu m bằng n-1 (m bắt dầu từ 0) thì sẽ thêm chuỗi này và chạy tiếp vòng lặp hoặc quay lui
            results.append("".join(strTest))
        if m < n-1: # Nếu m < n -1 thì tiếp tục đệ quy
              GenerateStr(n,m+1,stringAB,strTest)

# Đếm xem số lượng chữ số A liên tiêp lớn nhất là bao nhiều
def CountA(string):
    count = 0
    MaxLength = 0
    # Nếu là A thì cộng 1
    # Nếu là B thì so sánh với MaxLength nếu lớn hơn thì sẽ gán và cho count = 0 để đếm tiếp
    for i in string:
        if i== "A":
            count +=1
        if i== "B":
            if MaxLength < count:
                MaxLength = count
            count = 0
    if MaxLength < count:
            MaxLength = count
    return MaxLength

# Xử lý chuỗi
def processString(k):
    # Loại bỏ các chuỗi  mà sao cho trong đó có ít hơn 1 hay lơn hơn 1 lần xuất hiện  chuỗi (k chữ số A liên tiếp) 
    strA = "".join(["A"for i in range(0,k)])
    results1 = []
    for i in results:
        if i.count(strA) == 1:
            results1.append(i)
    
    # Đếm và kiểm tra nếu bằng k thì tm không thì loại
    results2 = []
    for i in results1:
        if CountA(i)==k:
            results2.append(i)
    
    return results2







        



    