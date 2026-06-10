class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr=nums.sort()
        def rec(index, arr):
            results.append(arr)
            print(results,index)
            if index>len(nums):
                return
            
            for i in range(index,len(nums)):
                print(i)
                if i > index and nums[i]==nums[i-1]:
                    continue   
                else:
                    rec(i+1, arr+[nums[i]])
        results=[]
        rec(0,[])
        return results


        