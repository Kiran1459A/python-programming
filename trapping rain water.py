n=list(map(int,input().split(",")))
l=len(n)
tw=0
le=[n[0]]
r=[n[l-1]]
for i in range(1,l):
    le.append(max(le[i-1],n[i]))
    r.append(max(r[i-1],n[l-i-1]))
    
for i in range(l):
    tw+=min(le[i],r[l-i-1])-n[i]
print(tw)
    
