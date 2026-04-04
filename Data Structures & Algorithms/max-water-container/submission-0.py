class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #to pointers 
        l, r= 0 , len(heights) -1 

        resp= 0
        
        while l < r:
            #are is the distance * minimun hight 

            area = min(heights[l], heights[r]) * (r-l)
            resp= max(resp,area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return resp
