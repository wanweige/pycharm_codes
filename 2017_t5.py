#牛客网2017真题
#分苹果
def fun(fruit):
    total = sum(fruit)
    count =0
    if total%n!=0:
        print(-1)
        exit(0)
    else:
        ave=total//n
        for i in fruit:
            if(i-ave)%2!=0:
                print(-1)
                exit(0)
            elif i>ave:
                count+=i-ave
        times=count//2
        print(times)
n=int(input())
fruit=list(map(int,input().split()))
fun(fruit)

#输入可这样写
'''
line = sys.stdin.readline()
n = int(line)
nums = [int(t) for t in sys.stdin.readline().split()]
'''