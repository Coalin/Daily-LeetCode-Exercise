class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_table = dict()
        for key in tasks:
            if key not in hash_table:
                hash_table[key] = 1
            else:
                hash_table[key] += 1
        
        max_key = ''
        max_cnt = 0
        for key in hash_table:
            if hash_table[key] > max_cnt:
                max_key = key
                max_cnt = hash_table[key]
        
        max_cnt_key_cnt = 0
        for key in hash_table:
            if hash_table[key] == max_cnt:
                max_cnt_key_cnt += 1

        return max(max_cnt_key_cnt+(max_cnt-1)*(1+n), len(tasks))