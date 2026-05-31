class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comw=strs[0]
        for st in strs:
            common=0
            for i in range(min(len(st),len(comw))):
                if st[i]==comw[i]:
                    common=common+1
                else:
                    break
            comw=comw[0:common]
        if common==-1:return ""
        else:return comw
                
                
                

            
            
            