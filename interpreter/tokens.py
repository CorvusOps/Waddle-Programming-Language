TOKEN_INT       = 'TOKEN_INT'
TOKEN_FLOAT     = 'FLOAT'
TOKEN_PLUS      = 'PLUS'
TOKEN_MINUS     = 'MINUS'
TOKEN_MULTI     = 'MULTI'
TOKEN_DIV       = 'DIV'
TOKEN_LEFTPAREN = 'LEFTPAREN'
TOKEN_RIGHTPAREN= 'RIGHTPAREN'

class Token: 
    """
    Attributes:

    Methods:

    Args:

    Returns:
    
    """
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
