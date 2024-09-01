"""You are given an unsorted array of integers and a positive integer K. Your task is to find the Kth largest element in the array.
The Kth largest element is the element that would appear in the Kth position if the array were sorted in descending order.
You need to implement a function that returns this Kth largest element without explicitly sorting the entire array.
Example
arr = [3, 2, 1, 5, 6, 4]
k = 2
Output: 5
"""
def largest(k,arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    if k>len(arr):
        return -1
    else:
        return arr[k-1]
    
print(largest(2,[3,2,1,5,6,4]))
