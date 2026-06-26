class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxcount=0
        left,right=0,len(height)-1
        while left<right:
            if (min(height[left],height[right])*(right-left))>maxcount:
                maxcount=min(height[left],height[right])*(right-left)
            if height[right]<height[left]:
                right-=1
            elif height[right]>height[left]:
                left+=1
            else:
                left+=1
        return maxcount