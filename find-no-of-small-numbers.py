class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count=count+1
            s.append(count)
        return s
        
