s=input()
flag=1
cp=0
nu=0
for i in range(len(s)):
    if s[0].isdigit():
        flag=0
    elif (s[i].isupper()):
        cp+=1
    elif s[i]==" " or s[i]=="/":
        flag=0
    elif (s[i].isdigit()):
        nu+=1

if flag:
    if cp>=1 and nu>=1:
        print("1")
    else:
        print("0")
else:
    print("0")
    
        
        
