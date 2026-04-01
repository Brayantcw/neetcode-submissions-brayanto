class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}

        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1
        #sort the dictionary and return the first k positions

        sorted_counter = sorted(counter, key=lambda x: counter[x], reverse=True)
        
        return sorted_counter[:k]