
####NODES

from interpreter.tokens import TOKEN_DIV, TOKEN_FLOAT, TOKEN_INT, TOKEN_MINUS, TOKEN_MULTI, TOKEN_PLUS


class NumberNodes:

    def __init__(self, tokens):
        self.tokens = tokens
    def __repr__(self):
        return f'{self.tokens}'

class binOpNode:
    def __init__(self, leftNode, opToken, rightNode):
        self.leftNode = leftNode
        self.opToken = opToken
        self.rightNode = rightNode
    def __repr__(self):
        return f'({self.leftNode}, {self.opToken},{self.rightNode})'


###PARSER###

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens_idx = 1
        self.advance()

    def advance(self):      #basically just moves to next chara or token
        self.tokens_idx += 1
        if self.tokens_idx < len(self.tokens):
            self.current_tokens = self.tokens[self.tokens_idx]   
        return self.current_tokens

    def parse(self):
        res = self.exp()
        return res

    def factor(self):
        token = self.current_tokens

        if token.type in (TOKEN_INT, TOKEN_FLOAT):
            self.advance()
            return NumberNodes(token)
        
    def term(self):
        return self.binaryOp(self.factor, (TOKEN_MULTI, TOKEN_DIV))

    def exp(self):
         return self.binaryOp(self.factor, (TOKEN_PLUS, TOKEN_MINUS))

    def binaryOp(self, func, operators):
        left = func()
        
        while self.current_tokens.type in operators:
            opToken = self.current_tokens
            self.advance()
            right = func()
            left = binOpNode(left, opToken, right)
    