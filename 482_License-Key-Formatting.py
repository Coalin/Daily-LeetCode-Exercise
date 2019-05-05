# Exercise I:
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        dash_len = 0
        word = ''
        
        for s in S:
            if s != '-':
                if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    word += s
                else:
                    word += s.upper() 
                    
        if word == '':
            return word
    
        word_len = len(word)
        
        first = word_len%K
        if first == 0:
            first = K
        total_count = word_len//K
        
        res = word[:first]
        count = 1
        
        while count <= total_count:
            res = res+'-'+word[first+count*K-K:first+count*K]
            count += 1
        
        if res[-1] == '-':
            return res[:-1]
        else:
            return res
            
 
# Exercise II:
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S:
            return S
        
        S_ = "".join(S.split('-'))
        
        if not S_:
            return S_
        
        res = ''
        for i in range(len(S_)%K):
            res += S_[i].upper()
            
        for j in range(len(S_)%K, len(S_)):
            if j%K == len(S_)%K:
                res += '-'
            res += S_[j].upper()
        
        if res:
            if res[0] == '-':
                return res[1:]

        return res           
                
            
        
