def greatest(list):
    r=0
    
    n=len(g)
    for i in range(n):
        if g[i]>r:
            r=g[i]
    return r
g=[8,12,13,15,31,21,51,3,5,7,5]
n=len(g)

result=greatest(g)
print("Greatest: ",result)
