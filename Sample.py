# Problem 1: Grouping anagrams together
# Main logic used here is putting the anagrams in a hashmap by using their primeproducts as keys and the values as the anagrams themselves

# Time Complexity: O(nk)
# Space Complexity: O(nk)
# Successfully ran on leetcode?: Yes
# Any problems faced solving this?: No

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def primeProduct(x:str) -> int:
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
            31, 37, 41, 43, 47, 53, 59, 61, 67, 
            71, 73, 79, 83, 89, 97, 101]

            res=1
            for i in x:
                res*=primes[ord(i)-ord('a')]
            
            return res
        
        smap={}
        for s in strs:
            key=primeProduct(s)
            if key not in smap:
                smap[key]=[s]
            else:
                smap[key].append(s)
        res=[]
        for k in smap:
            res.append(smap[k])
        
        return res



# Problem 2: Isomorphic String Check
# Maintain two hashmaps/dictionaries, one for s and one for t. iterate through the strings and map schar to tcahr and vice versa. If one of them is already mapped to another character, return False

# Time Complexity: O(n)
# Space Complexity: O(n)
# Successfully ran on leetcode?: Yes
# Any problems faced solving this?: No

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sl=len(s)
        tl=len(t)
        smap={}
        tmap={}
        
        for i in range(sl):
            schar=s[i]
            tchar=t[i]

            if schar in smap:
                if smap[schar]!=tchar:
                    return False
            else:
                smap[schar]=tchar
            
            if tchar in tmap:
                if tmap[tchar]!=schar:
                    return False
            else:
                tmap[tchar]=schar

        return True
            


# Problem 3: Word Patter
# Same logic as isomorphic strings but here the word in s is being stored as key or value

# Time Complexity: O(n)
# Space Complexity: O(n)
# Successfully ran on leetcode?: Yes
# Any problems faced solving this?: No

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist=s.split()
        smap={}
        pmap={}
        pl=len(pattern)
        sl=len(slist)

        if pl!=sl:
            return False

        for i in range(pl):
            pchar=pattern[i]
            sword=slist[i]

            if pchar in pmap:
                if pmap[pchar]!=sword:
                    return False
            else:
                pmap[pchar]=sword

            if sword in smap:
                if smap[sword]!=pchar:
                    return False
            else:
                smap[sword]=pchar

        return True


