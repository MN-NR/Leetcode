class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        
        def dfs(st,left_count,right_count):
            if n==left_count and n==right_count:
                print(st)
                result.append(st)
                return
                
            if left_count<n:
                print("open", left_count, right_count, st)
                dfs(st+"(",left_count+1,right_count)
            if left_count>right_count:
                dfs(st+")",left_count,right_count+1)
        dfs("",0,0)
        return result

            
        