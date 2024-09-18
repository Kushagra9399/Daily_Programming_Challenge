'''
Problem : Group Anagrams
You are given an array of strings strs[].
Your task is to group all the strings that are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Input :
strs[] = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output :
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''
def day10(arr):
    def sim(m,n):
        if len(m)!=len(n):
            return False
        else:
            for i in m:
                if i not in n:
                    return False
            return True
                    
    if len(arr)<=1:
        return [arr]
    else:
        p = [[]]
        for i in range(len(arr)):
            if len(p[0])==0:
                p[0].append(arr[i])
                continue
            l = False
            for j in p:
                if sim(j[0],arr[i]):
                    j.append(arr[i])
                    l = True
                    continue
            if l==False:
                p.append([arr[i]])
        return p

print(day10(["eat", "tea", "tan", "ate", "nat", "bat"]))
