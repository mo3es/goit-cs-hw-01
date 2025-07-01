from my_token import MyTokenType


class MyInterpreter():

    def __init__(self, tree_root):
        self.tree_root = tree_root


    def visit_BinOps(self,node):
        if node.operation.token_type == MyTokenType.DIVISION:
            if node.right_val == 0:
                raise ZeroDivisionError("Operation prohibited -division by zero.")
            return self.visit(node.left_node) / self.visit(node.right_node)
        elif node.operation.token_type == MyTokenType.MULTIPLICATION:
            return self.visit(node.left_node) * self.visit(node.right_node)
        elif node.operation.token_type == MyTokenType.PLUS:
            return self.visit(node.left_node) + self.visit(node.right_node)
        elif node.operation.token_type == MyTokenType.MINUS:
            return self.visit(node.left_node) - self.visit(node.right_node)
        elif node.operation.token_type == MyTokenType.POWER:
            return self.visit(node.left_node) ** self.visit(node.right_node)
        

    def visit_Numeric(self, node):
        return node.value


    def visit_UnaryOps(self, node):
        if node.operation.token_type == MyTokenType.PLUS:
            return self.visit(node.expression)
        elif node.operation.token_type == MyTokenType.MINUS:
            return (- 1 ) * self.visit(node.expression)


    def interpret(self):
        return self.visit(self.tree_root)


    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'Incorrect operation type: {type(node).__name__}')