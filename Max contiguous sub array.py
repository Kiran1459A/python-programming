n=list(map(int,input().split()))
d={}
l=len(n)
for i in range(l):
    for j in range(i+1,l):
        d[tuple(n[i:j])]=sum(n[i:j])
key=list(d.keys())
values=list(d.values())
m=values.index(max(values))
print(values[m])
