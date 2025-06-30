from my_token import MyToken, MyTokenType

class LexicalError(Exception):
    pass

class Lexer():

    # Оновлюємо OPERATORS_MAP
    OPERATORS_MAP = {
        '+': MyTokenType.PLUS,
        '-': MyTokenType.MINUS,
        '*': MyTokenType.MULTIPLY,
        '/': MyTokenType.DIVISION,
        '^': MyTokenType.POWER,
        '(': MyTokenType.LPARENTH,
        ')': MyTokenType.RPARENTH,
    }

    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = text[self.position] if text else None

    def advance(self):
        self.position += 1
        if self.position >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.position]

    # Додамо метод peek, щоб "заглядати" на наступний символ без просування
    def peek(self):
        peek_pos = self.position + 1
        if peek_pos >= len(self.text):
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return MyToken(MyTokenType.INTEGER, self.integer())

            # *** Логіка для розпізнавання ** (подвійна зірочка) ***
            if self.current_char == '*':
                if self.peek() == '*': # Якщо наступний символ також '*'
                    self.advance() # Просуваємося на першу '*'
                    self.advance() # Просуваємося на другу '*'
                    return MyToken(MyTokenType.POWER, '^')
                else: # Якщо після '*' немає іншої '*'
                    self.advance() # Просуваємося на '*'
                    return MyToken(MyTokenType.MULTIPLY, '*')


            if self.current_char in self.OPERATORS_MAP:
                token_type = self.OPERATORS_MAP[self.current_char]
                value = self.current_char
                self.advance()
                return MyToken(token_type, value)

            raise LexicalError(f"Lexical error: Unexpected character '{self.current_char}' at position {self.position}")

        return MyToken(MyTokenType.EOF, None)