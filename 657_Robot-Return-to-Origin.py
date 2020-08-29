class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lon = 0 
        lat = 0
        for s in moves:
            if s == 'R':
                lon += 1
            if s == 'L':
                lon -= 1
            if s == 'U':
                lat += 1
            if s == 'D':
                lat -= 1
        return lon == 0 and lat == 0
        