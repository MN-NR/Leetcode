class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index,arr):
            results.append(arr) 
            if index>=len(nums):
                return  
            for i in range(index,len(nums)):                         
                dfs(i+1,arr+[nums[i]])  
             
        results=[]
        dfs(0,[])            
        return results