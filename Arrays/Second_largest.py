# Problem Statement:

# Given an array arr of size N, find and return the second largest distinct element in the array. If no such element exists, return -1.

# Example 1

# Input:

# N = 5
# arr = [1, 2, 4, 7, 7]

# Output:

# 4

# Explanation:
# The largest element is 7, and the second largest distinct element is 4.

# Example 2

# Input:

# N = 5
# arr = [5, 5, 5, 5, 5]

# Output:

# -1

# Explanation:
# There is no second largest distinct element.

# Example 3

# Input:

# N = 6
# arr = [10, 20, 30, 40, 50, 50]

# Output:

# 40
# Constraints
# 2 ≤ N ≤ 10⁵
# -10⁹ ≤ arr[i] ≤ 10⁹

# Your Task
# Return the second largest distinct element without sorting the array if possible.

#CODE

def second_larg(arr):
    largest=float('-inf')
    second_largest=float('-inf')
    for i  in range(0,len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        if arr[i]<largest and arr[i]>second_largest:
            second_largest=arr[i]
    return second_largest if second_largest != float('-inf') else -1
arr=list(map(int,input("enter array: ").split()))
print(second_larg(arr))
    