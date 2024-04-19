g=[18,12,13,15,18,20,26]
n=len(g)
target=18
r=0
for i in range(n):
    if g[i]==target:
        r=r+1
print(r)
