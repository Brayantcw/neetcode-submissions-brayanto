class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        resp=[]
        visited= set()

        for i in range(len(strs)):

            if i in visited:
                continue

            inside_list=[]
            inside_list.append(strs[i])
            word1= list(strs[i])
        
            for j in range(i+1,len(strs)):
                if j in visited:
                    continue
                word2= list(strs[j])
                if sorted(word1) == sorted(word2):
                    inside_list.append(strs[j])
                    visited.add(j)

            resp.append(inside_list)
            visited.add(i)
        return resp