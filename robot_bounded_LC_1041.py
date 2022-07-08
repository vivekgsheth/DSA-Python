'''
Problem: https://leetcode.com/problems/robot-bounded-in-circle/
Solution: https://www.youtube.com/watch?v=nKv2LnC_g6E
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dirX, dirY = 0, 1
        
        for instruction in instructions:
            if instruction == 'G':
                x, y = x + dirX, y + dirY
            
            elif instruction == 'L':
                dirX, dirY = -1*dirY, dirX
            
            else:
                dirX, dirY = dirY, -1*dirX
            
        return (x,y) == (0,0) or (dirX, dirY) != (0, 1)
    
'''
TC: O(N)
SC: O(1)
'''