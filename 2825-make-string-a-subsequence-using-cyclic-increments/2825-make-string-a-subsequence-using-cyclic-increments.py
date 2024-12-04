class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i=0
        j=0
        while i<(len(str1)) and j< (len(str2)):
            if str1[i] == str2[j] or ord(str1[i])+1 == ord(str2[j]) or ord(str1[i])-25 == ord(str2[j]):
                j+=1
            i+=1
        return j==len(str2)