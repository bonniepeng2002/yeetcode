class Solution:
    def calculate(self, s: str) -> int:
        # # split s by the first operator by priority you see
        # # recursively calculate on s1 and s2, then combine them by the operator
        
        # if '-' in s:
        #     # split by delimiter, and perform max 1 split. Then get 0th or 1st element
        #     s1 = s.split("-", 1)[0]
        #     s2 = s.split("-", 1)[1]
        #     return self.calculate(s1) - self.calculate(s2)
        # if '+' in s:
        #     s1 = s.split("+", 1)[0]
        #     s2 = s.split("+", 1)[1]
        #     return self.calculate(s1) + self.calculate(s2)
        # if '/' in s:
        #     s1 = s.split("/", 1)[0]
        #     s2 = s.split("/", 1)[1]
        #     return self.calculate(s1) // self.calculate(s2)
        # if '*' in s:
        #     s1 = s.split('*', 1)[0]
        #     s2 = s.split("*", 1)[1]
        #     return self.calculate(s1) * self.calculate(s2)
        # return int(s)

        stack = []
        num = ""
        sign = '+'

        # iterate, and gather numbers. 
        # once finished a number, check the sign
        # if + or - sign, add it to the stack
        # once seen a */ sign, make note of it, and then gather the next number
        # once gathered, get the last sign, do the operation on current number and first item on stack, then put that on the stack

        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
                continue
            # s[i] is not a digit
            if s[i] == ' ':
                continue
            if sign == '+':
                stack.append(int(num))
            if sign == '-':
                stack.append(int(num) * -1)
            if sign == '*':
                stack.append(stack.pop() * int(num))
            if sign == '/':
                stack.append(int(stack.pop() / int(num)))
            num = ""
            sign = s[i]

        if num != "":
            if sign == '+':
                stack.append(int(num))
            if sign == '-':
                stack.append(int(num) * -1)
            if sign == '*':
                stack.append(stack.pop() * int(num))
            if sign == '/':
                stack.append(int(stack.pop() / int(num)))
        
        # sum up the stack
        return sum(stack)
