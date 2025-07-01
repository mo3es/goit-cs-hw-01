from enum import Enum


class MyTokenType(Enum):
    INTEGER = 'INTEGER'
    PLUS = '+'
    MINUS = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    POWER = '^'
    LPARENTH = '('
    RPARENTH = ')'
    EOF = 'EOF'



class MyToken():

    def __init__(self, token_type: MyTokenType, value):
        self.token_type = token_type
        self.value = value


    def __str__(self):
        return f'Token({self.token_type.name}, {repr(self.value)})'


    def __repr__(self):
        return self.__str__()