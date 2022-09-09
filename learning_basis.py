somme = 0
index = 0
def foo(A,n):
    m=A[0]
    x=0
    for i in range(n):
        x = x+A[i]
        if m<x:
            m=x

        if x< 0:
            x=0

    return m

A = [-12,-3,5,10,8,-16,-23,12,-5,7]
# print(foo(A, 10))

def foo2(n,d):
    x=0
    while(n>=1):
        x=x+1
        n=n//d

    return x

print(foo2(1037,2))
