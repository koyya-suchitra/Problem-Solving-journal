#lc 189
def rotate_array(arr,k):
    n=len(arr)
    k%=n
    def reverse(l,r):
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
    reverse(0,n-1)
    reverse(0,k-1)        
    reverse(k,n-1)
    return arr
nums=list(map(int,input("enter array: ").split()))
k=int(input("enter no of steps: "))
print(rotate_array(nums,k))