# Missing Number in an Array

# Problem Statement:

# Given an array nums containing N distinct numbers taken from the range [0, N], find the only number missing from the array.

# Example 1

# Input:

# nums = [3, 0, 1]

# Output:

# 2

# Explanation:
# Numbers should be [0, 1, 2, 3], so 2 is missing.

# Example 2

# Input:

# nums = [0, 1]

# Output:

# 2
# Example 3

# Input:

# nums = [9,6,4,2,3,5,7,0,1]

# Output:

# 8
# Constraints
# N == len(nums)
# 1 <= N <= 10^5
# 0 <= nums[i] <= N
# All numbers are unique.

'''
def miss_num(arr):
    n=len(arr)
    expected_Sum=(n*(n+1))//2
    actual_sum=sum(arr)
    return expected_Sum-actual_sum
arr=list(map(int,input("enter array: ").split()))
print(miss_num(arr))

'''
def miss_num(arr):
    n=len(arr)
    xor_a=0
    xor_b=0
    for i in range(len(arr)+1):
        xor_a^=i #xor of all nos from 0 to n gives "a number"
    for j in range(len(arr)):
        xor_b^=arr[j] #xor of numbers in array gives "a number" 
    return xor_a^xor_b #xor of both "0" and "a number" gives" missing number"
arr=list(map(int,input("enter array: ").split()))
print(miss_num(arr))
