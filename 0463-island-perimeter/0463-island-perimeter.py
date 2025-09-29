class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i,j):
            
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
                return 1
            if (i,j) in visited:
                return 0

            visited.add((i,j))
            perim = 0
            perim += dfs(i,j+1)
            perim += dfs(i+1,j)
            perim += dfs(i,j-1)
            perim += dfs(i-1,j)
            return perim



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    return dfs(r,c)
        return 0
        