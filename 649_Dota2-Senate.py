# Exercise I:
# Aug 5, 2023

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()

        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                rq.append(i)
            else:
                dq.append(i)

        while rq and dq:
            if rq[0] < dq[0]:
                dq.popleft()
                rq.append(rq[0]+n)
                rq.popleft()
            else:
                rq.popleft()
                dq.append(dq[0]+n)
                dq.popleft()

        return 'Radiant' if rq else 'Dire'
