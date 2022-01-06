#Class
from interpreter.errors import IllegalCharError
from interpreter.tokens import Token

#TOKEN CONSTANTS
from interpreter.tokens import TOKEN_DIV, TOKEN_FLOAT, TOKEN_INT, TOKEN_LEFTPAREN, TOKEN_MINUS, TOKEN_MULTI, TOKEN_PLUS, TOKEN_RIGHTPAREN

#CONSTANTS
DIGITS = '012342546879'

class Lexer:
    """Construct string of words (source code) into TOKENS

    This class do a very simple job : read the text version of the program, \
        then break them to parts of separate tokens.
    
    More class info soon....

    Attributes:
        text: a line/source code (e.g. 1 + 1, sample.wdl ) \
            in shell that will be converted.
    """

    def __init__(self, text):
        """Constructor function(built-in class structure)"""
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        """Reads the current character"""
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        """Assign the input TEXT to respective TOKENS
        
        Returns:
            List of TOKENS (mark)

        Raises:
            IllegarCharError: if the character is not recognized.
        """
        mark = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                mark.append(self.make_number())
            elif self.current_char == '+':
                mark.append(Token(TOKEN_PLUS))
                self.advance()
            elif self.current_char == '-':
                mark.append(Token(TOKEN_MINUS))
                self.advance()
            elif self.current_char == '*':
                mark.append(Token(TOKEN_MULTI))
                self.advance()
            elif self.current_char == '/':
                mark.append(Token(TOKEN_DIV))
                self.advance()
            elif self.current_char == '(':
                mark.append(Token(TOKEN_LEFTPAREN))
                self.advance()
            elif self.current_char == ')':
                mark.append(Token(TOKEN_RIGHTPAREN))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return mark, None

    def make_number(self):
        """Identify if the DIGITS is int or float
        
        Returns:
            Token of INT or FLOAT
        """
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TOKEN_INT, int(num_str))
        else:
            return Token(TOKEN_FLOAT, float(num_str))

def run(text):
    """Run the Lexer

    Arguments:
        text: inputed values in the console
    
    Returns:
        The Token-ized value of the text.

    Raises:
        IllegalCharError: if the character is not recognized.

    """
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error
