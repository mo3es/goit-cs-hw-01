class Numeric():

    def __init__(self, token):
        self.token = token
        self.value = token.value


    def __repr__(self):
        return f"Numeric({self.value})"



class BinOps():

    def __init__(self, left_node, operation, right_node):
        self.left_node = left_node
        self.operation = operation
        self.right_node = right_node




class UnaryOps():

    def __init__(self, operation, expression):
        self.operation = operation
        self.expression = expression