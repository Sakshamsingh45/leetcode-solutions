class Solution:
    def isValid(self, word: str) -> bool:
        v=0
        c=0
        d=0
        for i in word:
            if i.isalpha():
                if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                    v+=1
                elif ord(i.lower())<ord("z") and ord(i.lower())>ord("a") :
                    c+=1
            if i.isdigit():
                d=1
        return True if d!=0 and v!=0 and c!=0 else False