class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        path = path.split('/')
        for c in path:
            if c == '.' or c == '':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return '/'+'/'.join(stack)



s = Solution()
str = '/home/.//abc/../xyz//'
print(s.simplifyPath(str))