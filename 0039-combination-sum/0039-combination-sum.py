class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i,arrsum,arr):
            if arrsum==target:
                result.append(arr)
            elif arrsum>target or i+1>len(candidates):
                return
            else:
                dfs(i,arrsum+candidates[i],arr+[candidates[i]])
                for j in range(i,len(candidates)-1):
                    dfs(j+1,arrsum+candidates[j+1],arr+[candidates[j+1]])
               
        result=[]
        for i in range(len(candidates)):
            dfs(i,candidates[i],[candidates[i]])
        return result