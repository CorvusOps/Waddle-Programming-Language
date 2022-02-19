class Error: 
    """Defined errors in this programming language

    More class info soon...

    Attributes:
        error_name: passes child classes to specify error name.
        details: pass the details of the error.
    """

    def __init__(self, error_name, details):
        """Constructor function(built-in class structure)"""
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        """Returns a formatted error details"""
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    """Illegal Character Error
    
    This class inherits Error, it Returns: Illegal Character Error
    """
    def __init__(self, details):
        super().__init__('Illegal Character', details)




