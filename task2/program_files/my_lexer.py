from my_token import MyToken, MyTokenType


class ParsingError(Exception):
    pass



class Lexer():

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

        
        self.single_char_tokens = {
            '+': MyTokenType.PLUS,
            '-': MyTokenType.MINUS,
            '*': MyTokenType.MULTIPLICATION,
            '/': MyTokenType.DIVISION,
            '(': MyTokenType.LPARENTH,
            ')': MyTokenType.RPARENTH,
            '^': MyTokenType.POWER 
        }


    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]


    def peek(self):
        peek_pos = self.pos + 1
        
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]


    def skip_whitespace(self):

        while self.current_char is not None and self.current_char.isspace():
            self.advance()


    def integer(self) -> int:
        result = ''

        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)


    def get_next_token(self) -> MyToken:

        while self.current_char is not None:
            self.skip_whitespace()

            if self.current_char is None:
                break

            if self.current_char.isdigit():
                return MyToken(MyTokenType.INTEGER, self.integer())

            if self.current_char == '*' and self.peek() == '*':
                self.advance()
                self.advance()
                return MyToken(MyTokenType.POWER, '^')

            if self.current_char in self.single_char_tokens:
                token_type = self.single_char_tokens[self.current_char]
                value = self.current_char
                self.advance()
                return MyToken(token_type, value)

            raise ParsingError(f"Incorrect symbol: '{self.current_char}' at {self.pos} position")

        return MyToken(MyTokenType.EOF, None)