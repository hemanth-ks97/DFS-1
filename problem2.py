class Solution:
# Time Complexity : O(n*m)
# Space Complexity : O(n*m)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R,C = len(mat), len(mat[0])
        queue = collections.deque()
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    queue.append((i,j))
                elif mat[i][j] == 1:
                    mat[i][j] = -1

        def inBounds(r,c):
            return 0<=r<R and 0<=c<C
        
        while queue:
            r,c = queue.popleft()
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                dr,dc = r+di, c+dj
                if inBounds(dr,dc) and mat[dr][dc] == -1:
                    mat[dr][dc] = mat[r][c] + 1
                    queue.append((dr,dc))
        
        return mat