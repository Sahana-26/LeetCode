class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                if num in rows[i]:
                    return False
                if num in columns[j]:
                    return False
                subgrid_index = (i // 3) * 3 + j // 3
                if num in subgrids[subgrid_index]:
                    return False
                
                rows[i].add(num)
                columns[j].add(num)
                subgrids[subgrid_index].add(num)
        
        return True
