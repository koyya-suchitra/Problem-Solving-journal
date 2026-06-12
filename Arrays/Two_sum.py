def two_sum(arr,target):
    dic={}
    for i in range(len(arr)):
        comp=target-arr[i]
        if comp in dic:
            return {i,dic[comp]}
        else:
            dic[arr[i]]=i
arr=[2,11,7,15]
target=9
print(two_sum(arr,target))





arr=list(map(int,input("enter array: ").split()))
target=int(input("enter integer"))
print(two_sum(arr))