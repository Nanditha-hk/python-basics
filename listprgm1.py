def totaloccurences(list):
    r=0
    n=len(g)
    for i in range(n):
        if g[i]%2==0:
            print(g[i])
            r=r+1
    return r

g=[18,12,13,15,18,20,26,3,5,7,5]
n=len(g)

result=totaloccurences(g)
print(result)
