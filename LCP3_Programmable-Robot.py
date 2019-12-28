class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        # zb = [0, 0]
        # ind = 0
        # while True:
        #     if command[ind] == 'U':
        #         zb = [zb[0], zb[1]+1]
        #     elif command[ind] == 'R':
        #         zb = [zb[0]+1, zb[1]]
        #     # print(zb)
        #     if zb == [x, y]:
        #         return True 
        #     if zb in obstacles:
        #         return False
        #     if zb[0] > x or zb[1] > y:
        #         return False 
        #     if ind < len(command)-1:
        #         ind += 1
        #     elif ind == len(command)-1:
        #         ind = 0
        # return False

        xi = 0
        yi = 0
        zb = [0, 0]

        for c in command:
            if c == 'R':
                xi += 1
            if c == 'U':
                yi += 1
        epoch = min(x//xi, y//yi)
        x_ = x-epoch*xi
        y_ = y-epoch*yi 
        
        zb = [0, 0]
        is_reach = False

        for i in command:
            if zb == [x_, y_]:
                is_reach = True
            if i == 'R':
                zb = [zb[0]+1, zb[1]]
            if i == 'U':
                zb = [zb[0], zb[1]+1]


        obstacles_ = []
        for item in obstacles:
            if item[0]<=x and item[1]<=y:
                obstacles_.append(item)

        for ob in obstacles_:
            cur_epo = min(ob[0]//xi, ob[1]//yi)
            cur_x = ob[0]-cur_epo*xi
            cur_y = ob[1]-cur_epo*yi
            cur_zb = [0, 0]
            for cm in command:
                print(cur_zb)
                if cur_zb == [cur_x, cur_y]:
                    return False
                if cm == 'R':
                    cur_zb = [cur_zb[0]+1, cur_zb[1]]
                if cm == 'U':
                    cur_zb = [cur_zb[0], cur_zb[1]+1]
            
        return is_reach         
