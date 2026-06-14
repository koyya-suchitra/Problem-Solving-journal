#LEETCODE 26

# Original Array
# [0,0,1,1,1,2,2,3,3,4]

# Since the array is already sorted, duplicate numbers are next to each other.

# Your task is to:

# Keep only one copy of each number.
# Put all unique numbers at the beginning of the same array.
# Return how many unique numbers there are.
# What the array should look like

# After removing duplicates:

# [0,1,2,3,4,_,_,_,_,_]

# The _ means "we don't care what's here."

# There are 5 unique numbers, so return:

# 5
# Example 1

# Input:

# [1,1,2]

# Unique numbers:

# [1,2]

# Array becomes:

# [1,2,_]

# Return:

# 2
def remove_dups(arr):
    unique_ele=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[unique_ele]:
            unique_ele+=1
            arr[unique_ele]=arr[j]
        else:
            pass
    return unique_ele+1
arr=list(map(int,input("enter elements:").split()))
print(remove_dups(arr))