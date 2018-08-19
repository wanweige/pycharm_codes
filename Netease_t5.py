#射击游戏
def IslineAB(px,py):
    if py==px*k1+y[1]-k1*x[1]:
        return True
    else:
        return False
def IsPerpAB(px,py):
    temp=(py-y[2])(x[1]-x[0])+(px-x[2])(y[1]-y[0])
    if temp==0:
        return True
    else:
        return False
'''def IsPerpAB(px,py):
    k=(py-y[2])/(px-x[2])
    if k*k1==-1:
        return True
    else:
        return False'''
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
if n<=3:
    print(n)
else:
    k1=(y[1]-y[0])/(x[1]-x[0])
    count=3
    for j in range(3,n):
        if IslineAB(x[j],y[j]):
            count += 1
        elif IsPerpAB(x[j],y[j]):
            count += 1
    print(count)