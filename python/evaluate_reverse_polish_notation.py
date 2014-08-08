class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        import operator
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.div}
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(int(ops[token](x*1.0, y)))

        return stack.pop()

if __name__ == '__main__':
    s = Solution()
    print s.evalRPN(["2", "1", "+", "3", "*"])
    print s.evalRPN(["4", "13", "5", "/", "+"])
