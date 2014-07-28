class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        import operator
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.div 
        }
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(ops[token](x, y))
                
        return stack[0]
