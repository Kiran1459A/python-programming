# A denotes AND operation
# B denotes OR operation
# C denotes XOR Operation

str1="1C0C1C1A0B1"
a=int(str1[0])
i=0
while(i<len(str1)):
    if(str1[i]=="A"):
        a&=int(str1[i+1])
    elif(str1[i]=="B"):
        a|=int(str1[i+1])
    elif(str1[i]=="C"):
        a^=int(str1[i+1])
    i+=2
print(a)
