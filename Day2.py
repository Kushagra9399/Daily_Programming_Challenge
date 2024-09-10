'''
Problem: Find the missing number
You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

Input :
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output :
Return the missing integer from the array.
Example: Missing Number : 3
'''
def day2(arr):
    if arr[0]!=1:
        return 1
    elif arr[-1]!=len(arr)+1:
        return len(arr)+1
    else:
        for i in range(len(arr)-1):
            if arr[i+1]!=arr[i]+1:
                return arr[i]+1

print(day2([1,2,4,5]))
