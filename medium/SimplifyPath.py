class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack of paths, remove . and .. accordingly
        # return stack concatenated with '/'

        # O(number of /)
        pathArray = path.split('/')

        stack = []

        for curr in pathArray:
            if curr == "." or curr == "":
                continue
            elif curr == "..":
                if stack: # make sure to check all cases! especially when accessing an object, perform checks
                    stack.pop()
                continue
            else:
                stack.append(curr)

        return "/" + "/".join(stack)
