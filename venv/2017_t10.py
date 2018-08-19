#牛客网2017真题-题10
#幸运的袋子
'''
n=int(input("请输入球的数量："))
numbers=list(map(int,input("请输入球的号码：").split()))
numbers.sort()
he=numbers[0]+numbers[1]
ji=numbers[0]+numbers[1]
if n<=2:
    print(1)
else:
    for i in range(2,n):
        he += numbers[i]
        ji *= numbers[i]
        if he<=ji:
            flag=i
            break
    if i == n-1:
        curNum=n
    else:
        curNum=flag
    c=curNum-2
    total=2**c
    print("幸运福袋数为：%d"%total)'''



def dfs(x, pos, s, p):#s为和，p为积，pos为初始位置
    ans=0
    i=pos
    while i<n:
        nsum=s+x[i]
        nmul=p*x[i]
        if nsum>nmul:
            ans+=1+dfs(x,i+1,nsum,nmul)
        elif x[i]==1:
            ans+=dfs(x,i+1,s+1,p)
        else:
            break
        while i<n-1 and x[i]==x[i+1]:
            i+=1
        i+=1
    return ans
n=int(input("请输入球的数量："))
x = sorted(list(map(int, input("请输入球的号码：").split())))#对x从小到大进行排序
print(dfs(x,0,0,1))