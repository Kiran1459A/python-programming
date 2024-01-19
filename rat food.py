rat=int(input())
units=int(input())
n=7
arr=[2,8,3,5,7,4,1,2]
total_food_required=rat*2

s=arr[0]
count=1
for i in range(1,len(arr)):
    if total_food_required>s:
        s+=arr[i]
        
        count+=1
    else:
        break
print(count)
