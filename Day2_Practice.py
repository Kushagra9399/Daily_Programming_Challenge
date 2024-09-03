"""
You are given an unsorted array of integers. Your task is to find the median of the array.
The median is the middle value in an ordered list of numbers.
If the list has an even number of elements, the median is the average of the two middle numbers.
Example 1
arr = [3,2,1,4,5]
Output: 3
"""

def median(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    if len(arr)%2!=0:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2-1]+arr[len(arr)//2])/2

print(median([7,10,4,3,20,15]))
