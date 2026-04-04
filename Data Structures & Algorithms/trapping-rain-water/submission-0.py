class Solution:
    def trap(self, height: List[int]) -> int:
        
        resp=0 

        for i in range(len(height)):

            max_preview = max_post = height[i]
            #preview
            for j in range(i):
                max_preview= max(max_preview, height[j])
            #post
            for k in range(i+1,len(height)):
                max_post = max(max_post,height[k])

            resp += min(max_post, max_preview) - height[i]
        return resp