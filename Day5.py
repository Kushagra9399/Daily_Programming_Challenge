'''
Problem : Find the Leaders in an Array
You are given an integer array arr of size n.
An element is considered a leader if it is greater than all the elements to its right.
Your task is to find all such leader elements in the array.

Input :
An integer array arr of size n.
Example : 
arr = [16, 17, 4, 3, 5, 2]

Output :
Return an array containing all the leader elements in the order in which they appear in the original array.
Example:
Leaders: [17, 5, 2]
'''

def day5(arr):
    a = []
    for i in range(len(arr)):
        k = True
        for j in range(i+1,len(arr)):
            if arr[i]<=arr[j]:
                k = False
                break
        if k==True:
            a.append(arr[i])
    return a

print(day5([16, 17, 4, 3, 5, 2]))
