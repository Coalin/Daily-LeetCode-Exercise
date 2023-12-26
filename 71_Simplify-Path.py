# Exercise I:
# Dec 26, 2023

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        files = path.split('/')
        for file in files:
            if file == '.' or file == '':
                continue
            elif file == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(file)

        return '/' + '/'.join(stack)
