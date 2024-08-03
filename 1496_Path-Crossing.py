# Exercise I:
# Aug 3, 2024

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0, 0))
        x, y = 0, 0

        for p in path:
            if p == "N":
                y += 1
            elif p == "S":
                y -= 1
            elif p == "W":
                x -= 1
            elif p == "E":
                x += 1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
