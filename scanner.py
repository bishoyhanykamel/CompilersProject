import re


class Scanner:

    def __init__(self):
        self.set_state('START')
        self.tokens = []
        self.state_other = False
        self.identifiers = list()
        self.numbers = list()

    def set_state(self, state):
        for key in self.STATES:
            self.STATES[key] = False
        self.STATES[state] = True

    def get_state(self, state):
        return self.STATES[state]

    def scan(self, input_code):
        input_text = self.modify_code(input_code)
        token = ''
        for c in input_text:
            if self.get_state('START'):
                if self.is_symbol(c):
                    self.set_state('DONE')
                elif c == ' ':
                    self.set_state('START')
                    continue
                elif c == '{':
                    self.set_state('IN_COMMENT')
                elif self.is_num(c):
                    self.set_state('IN_NUMBER')
                elif self.is_str(c):
                    self.set_state('IN_IDENTIFIER')
                elif self.is_col(c):
                    self.set_state('IN_ASSIGNMENT')

            elif self.get_state('IN_COMMENT'):
                if c == '}':
                    self.set_state('DONE')
                else:
                    self.set_state('IN_COMMENT')

            elif self.get_state('IN_NUMBER'):
                if self.is_num(c):
                    self.set_state('IN_NUMBER')
                elif c == ' ':
                    self.set_state('DONE')
                else:
                    self.set_state('OTHER')

            elif self.get_state('IN_IDENTIFIER'):
                if self.is_str(c):
                    self.set_state('IN_IDENTIFIER')
                elif c == ' ':
                    self.set_state('DONE')
                else:
                    self.set_state('OTHER')

            elif self.get_state('IN_ASSIGNMENT'):
                if c == '=':
                    self.set_state('DONE')
                else:
                    self.set_state('OTHER')

            if not self.get_state('OTHER'):
                token += c

            if self.get_state('OTHER'):
                self.set_state('DONE')
                self.state_other = True

            if self.get_state('DONE'):
                self.classify(token)
                if self.state_other:
                    token = c
                    if self.is_col(c):
                        self.set_state('IN_ASSIGNMENT')
                    if self.is_comment(c):
                        self.set_state('IN_COMMENT')
                    if self.is_num(c):
                        self.set_state('IN_NUMBER')
                    if self.is_str(c):
                        self.set_state('IN_IDENTIFIER')
                    if self.is_symbol(c):
                        self.classify(c)
                        token = ''
                        self.set_state('START')
                    self.state_other = False
                else:
                    token = ''
                self.set_state('START')

    def classify(self, token):
        if token[-1:] == ' ':
            token = token[0:-1]
        if self.is_str(token):
            if token in self.RESERVED_KEYWORDS:
                self.tokens.append([token, "{}{}".format(token[0].upper(), token[1:])])
            elif token in self.DATA_TYPES:
                    self.tokens.append([token, "{}{}".format(token[0].upper(), token[1:])])
            else:
                self.tokens.append([token, 'Identifier'])
        elif self.is_num(token):
            self.tokens.append([token, 'Number'])
        elif token in self.OPERATORS:
            self.tokens.append([token, self.OPERATORS[token]])
        elif self.is_comment(token):
            self.tokens.append([token, 'Comment'])

    def is_str(self, token):
        return token.isalpha()

    def is_num(self, token):
        return token.isdigit()

    def is_col(self, c):
        return True if c == ':' else False

    def is_symbol(self, token):
        symbol = ['+', '-', '*', '/', '=', '<', '>', '(', ')', ';']
        return True if token in symbol else False

    def is_comment(self, token):
        return True if re.match(r'^{.+}$', token) else False

    def modify_code(self, code):
        tiny_code = code.replace('\n', ' ')
        tiny_code = "{} a".format(tiny_code)
        return tiny_code

    def output(self):
        self.call_for_errors()
        with open('output.txt', 'w') as f:
            f.write('{:<32} {:>32}\n'.format('==================', '=================='))
            f.write('{:<32}  {:>32}\n'.format('========[TYPE]=======', '========[TOKEN]======='))
            f.write('{:<32} {:>32}\n'.format('==================', '=================='))
            for token in self.tokens:
                f.write('{:<40}  {:>40}\n'.format(token[1], token[0]))

    def print_output(self):
        with open('output.txt', 'r') as f:
            return "".join(f.readlines())

    def call_for_errors(self):
        index = 0
        found_data_type = False
        found_identifier = False
        found_number = False
        found_comment = False
        found_symbol = False
        while index < len(self.tokens):
            if self.tokens[index][1] == 'Int':
                print("I found int")
            elif self.tokens[index][1] == 'Double':
                print("I found double")
            elif self.tokens[index][1] == 'Float':
                print("I found float")
            elif self.tokens[index][1] == 'Character':
                print("I found character")
            elif self.tokens[index][1] == 'String':
                print("I found string")
            elif self.tokens[index][1] == 'If':
                print("I found if")
            elif self.tokens[index][1] == 'Then':
                print("I found then")
            elif self.tokens[index][1] == 'Else':
                print("I found else")
            elif self.tokens[index][1] == 'End':
                print("I found end")
            elif self.tokens[index][1] == 'Read':
                print("I found read")
            elif self.tokens[index][1] == 'Write':
                print("I found write")
            elif self.tokens[index][1] == 'Repeat':
                print("I found repeat")
            elif self.tokens[index][1] == 'Until':
                print("I found until")
            elif self.tokens[index][1] == 'Plus Operator':
                print("I found plus")
            elif self.tokens[index][1] == 'Minus Operator':
                print("I found minus")
            elif self.tokens[index][1] == 'Multiplication Operator':
                print("I found times")
            elif self.tokens[index][1] == 'Division Operator':
                print("I found div")
            elif self.tokens[index][1] == 'Semi Colon Operator':
                print("I found semi colon")
            elif self.tokens[index][1] == 'Assignment Operator':
                print("i found assignment")
            elif self.tokens[index][1] == 'Colon':
                print("i found colon")
            elif self.tokens[index][1] == 'Equals Operator':
                print("I found equals operator")
            elif self.tokens[index][1] == 'Greater Than Operator':
                print("I found greater than operator")
            elif self.tokens[index][1] == 'Less Than Operator':
                print("I found less than operator")
            elif self.tokens[index][1] == 'Open bracket':
                print("I found open bracket")
            elif self.tokens[index][1] == 'Close bracket':
                print("I found close bracket")
            elif self.tokens[index][1] == 'Identifier':
                print("I found identifier")
            index += 1
            pass
        # note: the last element isnt checked by default
    pass

    STATES = {
        'START': False,
        'IN_COMMENT': False,
        'IN_IDENTIFIER': False,
        'IN_DATA_TYPE': False,
        'IN_NUMBER': False,
        'IN_ASSIGNMENT': False,
        'DONE': False,
        'ERROR': False,
        'OTHER': False
    }
    RESERVED_KEYWORDS = ['else', 'end', 'if', 'repeat', 'then', 'until', 'read', 'write']
    DATA_TYPES = ['int', 'double', 'float', 'character', 'string']
    OPERATORS = {
        '+': 'Plus Operator',
        '-': 'Minus operator',
        '*': 'Multiplication Operator',
        '/': 'Division Operator',
        ':': 'Colon',
        '=': 'Equals Operator',
        ':=': 'Assignment Operator',
        '>': 'Greater Than Operator',
        '<': 'Less Than Operator',
        ';': 'Semi Colon Operator',
        '(': 'Open bracket',
        ')': 'Close bracket'
    }
