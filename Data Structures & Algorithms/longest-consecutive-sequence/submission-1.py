class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if list is empty
        if not nums:
            return 0

        #variables 
        resp = 0
        nums.sort() # [1,1,2,3,4,5,5,6,7,8] <- this is how we want the list

        current, counter = nums[0], 0 #the first consecutive numbers 0 
        i=0 

        while i < len(nums):

            if current != nums[i]:
                current = nums[i]
                counter=0
            while i < len(nums) and nums[i] == current: # consecutive same number
                i+=1
            counter +=1
            current +=1
            resp = max(resp,counter)

        return resp 
            