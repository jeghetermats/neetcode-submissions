class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(len(board)):
            row = board[i]
            l = []
            for num in row:
                if num == ".":
                    continue
                if num in l:
                    return False
                l.append(num)

        #cols
        for i in range(len(board[0])):
            col = [board[j][i] for j in range(len(board))]
            l = []
            for num in col:
                if num == ".":
                    continue
                if num in l:
                    return False
                l.append(num)
            
        #3x3s
        for i in range(2):
            for j in range(2):
                nums = []
                for k in range(i*3,3+i*3):
                    for l in range(j*3,3+j*3):
                        num = board[k][l]
                        if num == ".":continue
                        if num in nums:return False
                        nums.append(num)
        return True
                