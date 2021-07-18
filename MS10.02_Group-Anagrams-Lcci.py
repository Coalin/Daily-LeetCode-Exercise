class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        res = []
            
        for s in strs:
            sorted_str = "".join((lambda x:(x.sort(), x)[1])(list(s)))
            if sorted_str in hash_table:
                hash_table[sorted_str].append(s)
            else:
                hash_table[sorted_str] = [s]

        for i in hash_table:
            res.append(hash_table[i])

        return res
