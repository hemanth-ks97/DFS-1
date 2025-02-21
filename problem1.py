# Time Complexity : O(n*m)
# Space Complexity : O(n*m)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R,C = len(image), len(image[0])

        visited = set()

        def isValid(r,c):
            return 0<=r<R and 0<=c<C

        def dfs(node, st_color, color):
            if not node or node in visited:
                return
            
            visited.add(node)
            r,c = node
            image[r][c] = color
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                dr,dc = r+di, c+dj
                if isValid(dr,dc) and (dr,dc) not in visited and image[dr][dc] == st_color:
                    dfs((dr,dc), st_color, color)

        st_color = image[sr][sc]
        if st_color != color:
            dfs((sr,sc), st_color, color)

        return image