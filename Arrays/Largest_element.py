# Problem Statement:

# Given an array arr of size N, print the largest element present in the array.

# Examples

# Example 1
# Input:

# N = 5
# arr = [1, 8, 7, 56, 90]

# Output:

# 90

# Explanation:
# 90 is the largest element in the array.

# Example 2
# Input:

# N = 5
# arr = [5, 5, 5, 5, 5]

# Output:

# 5

# Explanation:
# All elements are equal, so the largest element is 5.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9
# Your Task

# Write a function that returns the largest element in the array.

#CODE:
def largest_element(arr):
        largest=arr[0]
        for i in range(0,len(arr)):
                if arr[i]>largest:
                        largest=arr[i]
        return largest
arr=list(map(int,input("Enter elements: ").split()))
print(largest_element(arr))                     