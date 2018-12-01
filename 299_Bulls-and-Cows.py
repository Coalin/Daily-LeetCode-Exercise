class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_dic = {}
        guess_dic ={}
        A = 0
        B = 0
        
        for i in range(len(secret)):
            if secret[i] in secret_dic:
                secret_dic[secret[i]].append(i)
            else:
                secret_dic[secret[i]] = [i]
                
        for j in range(len(guess)):
            if guess[j] in guess_dic:
                guess_dic[guess[j]].append(j)
            else:
                guess_dic[guess[j]] = [j]
        
        print(secret_dic)
        print(guess_dic)
        
        for key in guess_dic:
            cur_A = 0
            if key in secret_dic:
                for x in guess_dic[key]:
                    if x in secret_dic[key]:
                        cur_A += 1
                A += cur_A
                B += min(len(secret_dic[key]),len(guess_dic[key]))-cur_A
        
        return str(A)+"A"+str(B)+"B"
                
