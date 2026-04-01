class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        needed= {}

        for i in range(len(nums)):
            resp=[]
            current= nums[i]
            missing = target - current
            if missing in needed:
                resp.append(needed[missing])
                resp.append(i)
                return resp
            needed[current]= i 