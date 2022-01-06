#TOKEN CONSTANTS
TOKEN_INT       = 'TOKEN_INT'
TOKEN_FLOAT     = 'FLOAT'
TOKEN_PLUS      = 'PLUS'
TOKEN_MINUS     = 'MINUS'
TOKEN_MULTI     = 'MULTI'
TOKEN_DIV       = 'DIV'
TOKEN_LEFTPAREN = 'LEFTPAREN'
TOKEN_RIGHTPAREN= 'RIGHTPAREN'

#UNINPLEMENTED
TOKEN_MODULO    = 'MODULO'
#relationals 

#logical

#identifier 

#keywords

#delimiters

#


class Token: 
    """
    Attributes:
        type_:
        value: default none.

    Methods: for reference only

    Args: for reference only

    Returns: for reference only
    
    """
    def __init__(self, type_, value=None):
        """Constructor function(built-in class structure)"""
        self.type = type_
        self.value = value

    def __repr__(self):
        """String representation of the type and value
        
            Returns:
                The new value of TYPE based on VALUE
            
            So we can pass the strings explicitly (you convert the variable to the target type)
            
            Review:
            f strings in python
            """
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
