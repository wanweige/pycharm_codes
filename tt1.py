#头条2018 第二批题 1用户喜好
# def fun(n,love,m,query):
#     first=query[0]
#     end=query[1]
#     check=query[2]
#     count=0
#     for each in love[first-1:end]:
#         if each==check:
#             count+=1
#     print(count)
#
# n=int(input())
# value=list(map(int,input().split()))
# array=int(input())
# for i in range(array):
#     flag=list(map(int,input().split()))
#     fun(n,value,array,flag)
def fun(n,love,m,query):
    if not query or not love:
        return None
    first=query[0]-1
    end=query[1]-1
    if first<0 or first>n:
        return None
    if end<0 or end>n:
        return None
    if first>end:
        return None
    check=query[2]
    count=low=high=0
    love.sort()
    count=high_t(love,check,first,end)-low_t(love,check,first,end)
    print(count)
def low_t(love,check,first,end):
    while first<end:
        mid=(first+end)>>1
        if love[mid]>=check:
            end=mid
        else:
            first=mid+1
    return first
def high_t(love,check,first,end):
    while first<end:
        mid=(first+end)>>1
        if love[mid]<=check:
            first=mid+1
        else:
            end=mid
    return first
n=int(input())
value=list(map(int,input().split()))
array=int(input())
for i in range(array):
    flag=list(map(int,input().split()))
    fun(n,value,array,flag)