class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(i):
            visited.add(i)
            for room in rooms[i]:
                if room not in visited:
                    dfs(room)
            
        visited = set()
        dfs(0)

        return len(visited) == len(rooms)
