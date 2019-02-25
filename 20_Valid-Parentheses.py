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
                

# Exercise II:
# Feb 25, 2019
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if not s:
            return True
        if len(s) == 1:
            return False
        
        str_stack = []
        
        if s[0] in ['(', '[', '{']:
            str_stack.append(s[0])
        else:
            return False
        
        index = 1
        while index <= len(s)-1:
            if s[index] in ['(', '[', '{']:
                str_stack.append(s[index])
            else:
                if str_stack:
                    if self.match(s[index], str_stack[-1]):
                        str_stack.pop()
                    else:
                        return False
                else:
                    return False
            index += 1
        if str_stack:
            return False
        else:
            return True
                
                
    def match(self, s1, s2):
        return (s1==')' and s2=='(') or (s1==']' and s2=='[') or (s1=='}' and s2=='{')
    
            
        
            
        
        
