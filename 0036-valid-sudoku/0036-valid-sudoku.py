class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        print("rows")
        for i in range(0,9):
            hash={}
            for j in range(0,9):
                if board[i][j]!=".":
                    if board[i][j] in hash:
                        return False
                    else:
                        hash[board[i][j]]=board[i][j]
            print(hash)
            hash.clear()
        print("columns")
        for i in range(0,9):
            hash={}
            for j in range(0,9):
                if board[j][i]!=".":
                    if board[j][i] in hash:
                        return False
                    else:
                        hash[board[j][i]]=board[j][i]
            print(hash)
            hash.clear()
        print("cubes")
        for row in range(0,9,3):
            for col in range(0,9,3):
                hash={}
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j]!=".":
                            if board[i][j] in hash:
                                return False
                            else:
                                hash[board[i][j]]=board[i][j]
                print(hash)
        
        return True
    

        