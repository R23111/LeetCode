class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings = sorted(meetings,key=lambda l:l[0])
        rooms = [[-1, -1, 0] for _ in range(n)]
        for meeting in meetings:
            for room in rooms:
                if room[1] <= meeting[0]:
                    room[0] = meeting[0]
                    room[1] = meeting[1]
                    room[2] += 1
                    break
            else:
                idx = self.minimum_index(rooms)
                rooms[idx][0] = rooms[idx][1]
                rooms[idx][1] = (meeting[1] - meeting[0]) + rooms[idx][1]
                rooms[idx][2] += 1
        counts = [r[2] for r in rooms]
        return counts.index(max(counts))
            
    
    def minimum_index(self, meetings):
        min_v = None
        min_idx = None
        for i, m in enumerate(meetings):
            if min_v is None:
                min_v = m[1]
                min_idx = i
                continue
            if min_v > m[1]:
                min_v = m[1]
                min_idx = i

        return min_idx