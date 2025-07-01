from my_token import MyTokenType as t_type
from my_lexer import Lexer
from my_ast import Numeric, BinOps, UnaryOps


class ParsingError(Exception):
    pass


class MyParser():

    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()


    def eat(self, token_type: t_type):
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ParsingError(f'Parsing error: expected - {token_type.value}; received - {self.current_token.token_type.value}')


    def term(self):
        """
        Обробляє оператори дужок, унарні та числа - найвищий пріорітет.

        """

        token = self.current_token

        # Унарні оператори
        if token.token_type == t_type.PLUS:
            self.eat(t_type.PLUS)
            return UnaryOps(operation=token, expression=self.term())

        elif token.token_type == t_type.MINUS:
            self.eat(t_type.MINUS)
            return UnaryOps(operation=token, expression=self.term())

        # Дужки
        elif token.token_type == t_type.LPARENTH:
            self.eat(t_type.LPARENTH)
            node = self.expression() # Вираз всередині дужок
            self.eat(t_type.RPARENTH)
            return node

        # Цілі числа
        elif token.token_type == t_type.INTEGER:
            self.eat(t_type.INTEGER)
            return Numeric(token)

        else:
            raise ParsingError(f'Unexpected token {token.token_type.value} at term level.')


    def power(self):
        """
        Обробляє оператор ступеня (пріоритет, наступний після term).

        """
        node = self.term()

        while self.current_token.token_type == t_type.POWER:
            operation_token = self.current_token
            self.eat(t_type.POWER)
            node = BinOps(left_node=node, operation=operation_token, right_node=self.power())

        return node


    def mult_div(self):
        """
        Обробляє оператор множення та ділення, середній пріорітет.

        """
        node = self.power()

        while self.current_token.token_type in (t_type.DIVISION, t_type.MULTIPLICATION):
            operation_token = self.current_token
            if self.current_token.token_type == t_type.DIVISION:
                self.eat(t_type.DIVISION)
            elif self.current_token.token_type == t_type.MULTIPLICATION:
                self.eat(t_type.MULTIPLICATION)

            node = BinOps(left_node=node, operation=operation_token, right_node=self.power())

        return node


    def expression(self):
        """
        Обробляє + та - (найнижчий пріоритет).

        """
        node = self.mult_div()

        while self.current_token.token_type in (t_type.PLUS, t_type.MINUS):
            operation_token = self.current_token
            if self.current_token.token_type == t_type.PLUS:
                self.eat(t_type.PLUS)
            elif self.current_token.token_type == t_type.MINUS:
                self.eat(t_type.MINUS)

            node = BinOps(left_node=node, operation=operation_token, right_node=self.mult_div())

        return node


    def parse(self):
        """
        Функція входу в парсер
        """
        node = self.expression()

        if self.current_token.token_type != t_type.EOF:
            raise ParsingError(f'Unexpected end of parsing, given expression is not fully parsed: exited on {self.current_token.token_type.value}')

        return node


    def print_parsing_tree(self, node, level=0):
        indent = '   ' * level

        if isinstance(node, Numeric):
            print(f'{indent}Numeric: {node.token.value}')
        elif isinstance(node, UnaryOps):
            print(f'{indent}UnaryOp: {node.operation.token_type.value}')
            print(f'{indent}   Expression:')
            self.print_parsing_tree(node.expression, level + 1)
        elif isinstance(node, BinOps):
            print(f'{indent}BinOp: {node.operation.token_type.value}')
            print(f'{indent}   Left:')
            self.print_parsing_tree(node.left_node, level + 1)
            print(f'{indent}   Operation: {node.operation.token_type.name}')
            print(f'{indent}   Right:')
            self.print_parsing_tree(node.right_node, level + 1)
        else:
            print(f'{indent} Unknown AST Node Type: {type(node)}')