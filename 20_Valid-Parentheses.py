class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = list(s)
        my_stack = []
        if s[0] in [')', ']', '}']:
            return False
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                my_stack.append(s[i])
            elif s[i] in [')', ']', '}']:
                if len(my_stack) == 0:
                    return False
                elif (s[i] == ')' and my_stack[-1] == '(') or (s[i] == ']' and my_stack[-1] == '[') or (s[i] == '}' and my_stack[-1] == '{'):
                    my_stack.pop()
                elif (s[i] == ')' and my_stack[-1] in ['[', '{']) or (s[i] == ']' and my_stack[-1] in ['(', '{']) or (s[i] == '}' and my_stack[-1] in ['(', '[']):
                    return False                
        if len(my_stack) != 0:
            return False
        else:
            return True
                
                
        
