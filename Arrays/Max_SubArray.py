def max_subarray(arr):
    currsum=0
    maxsum=float("-inf")
    for i in arr:
        currsum+=i
        if currsum>maxsum:
            maxsum=max(maxsum,currsum)
        if currsum<0:
            currsum=0
    return maxsum
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(arr))