arithmetic_operators = ['+', '-', '*', '/']
comparison_operators = ['<', '>', '=']
reserved_keywords = ['if', 'then', 'end', 'repeat', 'until']
reserved_semi_colon = ['read', 'write']
data_types = ['int', 'double', 'float', 'char', 'string', 'void']
assignment_operator = ':='
brackets = ['(', ')']
semi_colon = ';'
comments = ['{', '}']
found = list()
identifiers_found = []
numbers_found = []

code = """int x; 
if x > 0 then {don’t compute if x <= 0 }
fact := 1;
repeat 
fact := fact * x;
x := x –1; 
until x = 0 write fact; end"""


class Token:
    def __init__(self, value, start_index):
        self.value = value
        self.starting_index = start_index

    def __str__(self):
        # arithmetic
        if self.value == '+':
            return "Addition Operator"

        elif self.value == '-':
            return "Minus Operator"

        elif self.value == '*':
            return "Multiplication Operator"

        elif self.value == '/':
            return "Division Operator"

        # reserved keywords
        elif self.value in reserved_keywords or self.value in reserved_semi_colon:
            return "Reserved Keyword"

        # data types
        elif self.value in data_types:
            return "Data Type"

        # comparison operators
        elif self.value == '>':
            return "Greater Than Operator"

        elif self.value == '<':
            return "Less Than Operator"

        elif self.value == '=':
            return "Equal operator"

        elif self.value == '(':
            return "Open Bracket"

        elif self.value == ')':
            return "Closed Bracket"

        # comments
        elif self.value in comments:
            return "Comment"

        # assignment operator
        elif self.value == assignment_operator:
            return "Assignment Operator"

        # semi colon
        elif self.value == semi_colon:
            return "Semi Colon Operator"

        # variables
        elif self.value in identifiers_found:
            return "Identifier"

        # numbers
        elif self.value in numbers_found:
            return "Number"


class Scanner:
    def __init__(self, input_code):
        self.code = input_code
        self.code_size = len(input_code) - 1
        self.tokens_found = list()
        self.current_char = -1
        self.if_counter = 0
        self.skip = 0
        self.check_for_data_type = False

    def get_start_index(self, word):
        return self.current_char - len(word)

    def peak_character(self, index):
        return self.code[index + 1]

    def add_token(self, word):
        self.tokens_found.append(Token(word, self.get_start_index(word)))

    def print_tokens(self):
        for token in self.tokens_found:
            print("Token: {} ======= Type: ".format(token.value, token))





