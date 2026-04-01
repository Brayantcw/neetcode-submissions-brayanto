class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resp = []
        for i in range(len(nums)):
            #we need a holder
            holder = nums.pop(i)
            
            # multiply all remaining elements
            result = 1
            for num in nums:
                result *= num
            
            resp.append(result)
            
            nums.insert(i, holder)
        
        return resp