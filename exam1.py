#n,m=map(int,input().split())
#print(n,m)
#网易内推运维编程题
import sys
def game(n,m,values):
    c=[]
    n1=n+1
    for i in range(m):
        if values[i]>n or values[i]<1:
            return None

        #n=n+1
        for j in range(1,n1):
            temp=values.count(j)
            #c.append(temp)
            if temp==0:
                return 0
            c.append(temp)
    point=min(c)
    return point
n,m=map(int,input().split())
#list1=[]
line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
values = list(map(int, line.split()))
print(game(n,m,values))