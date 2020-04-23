#!/usr/bin/env python
# coding: utf-8

# In[61]:


# Token Types
# EOF shows end-of-file token
INTEGER, PLUS, MINUS, MUL, LPAREN, RPAREN, EOF = ('INTEGER', 'PLUS', 'MINUS', 'MUL', '(', ')', 'EOF')
VARIABLE, RESERVED = ('VARIABLE', 'RESERVED')
ASSIGNMENT = 'ASSIGNMENT'
EQUAL, LESS, MORE, NOT, AND, OR, TRUE, FALSE = ('EQUAL', 'LESS', 'MORE', 'NOT', 'AND', 'OR', 'TRUE', 'FALSE')
IF, THEN, ELSE, WHILE, DO = ('IF', 'THEN', 'ELSE', 'WHILE', 'DO')
SKIP, LBRA, RBRA, SEMICOLON = ('SKIP', 'LBRA', 'RBRA', 'SEMICOLON')


# In[62]:


reserved = ['true', 'false', 'if', 'then', 'else', 'while', 'do', 'skip']


# In[63]:


# Token class

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


# In[65]:


# Lexer

class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * -3 - 6"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        if self.current_char is '-':
            result += '-'
            self.advance()
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            
        return int(result)
    
    def var(self):
        '''Return a variable consumed from the input'''
        result = ''
        if self.current_char is not None and str(self.current_char).isalnum() and not self.current_char.isdigit():
            while self.current_char is not None and str(self.current_char).isalnum():
                result += self.current_char
                self.advance()   
        return result
                

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        isvariabale = True
        
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                isvariabale = False
                return Token(INTEGER, self.integer())
            
            if self.current_char == ':' and self.text[self.pos+1] == '=':
                isvariabale = False
                self.advance()
                self.advance()
                return Token(ASSIGNMENT, ':=')

            if self.current_char == '+':
                isvariabale = False
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-' and self.text[self.pos+1].isspace():
                isvariabale = False
                self.advance()
                return Token(MINUS, '-')
            
            if self.current_char == '-' and self.text[self.pos+1].isdigit():
                isvariabale = False
                self.advance()
                return Token(INTEGER, -self.integer())

            if self.current_char == '*':
                isvariabale = False
                self.advance()
                return Token(MUL, '*')
            
            if self.current_char == '(':
                isvariabale = False
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                isvariabale = False
                self.advance()
                return Token(RPAREN, ')')
            
            if self.current_char == '¬':
                isvariable = False
                self.advance()
                return Token(NOT, '¬')
            
            if self.current_char == '∧':
                isvariable = False
                self.advance()
                return Token(AND, '∧')
            
            if self.current_char == '∨':
                isvariable = False
                self.advance()
                return Token(OR, '∨')
            
            if self.current_char == '=' and self.text[self.pos-1].isspace():
                isvariable = False
                self.advance()
                return Token(EQUAL, '=')
            
            if self.current_char == '<':
                isvariable = False
                self.advance()
                return Token(LESS, '<')
            
            if self.current_char == '>':
                isvariable = False
                self.advance()
                return Token(MORE, '>')
            
            if self.current_char == '{':
                isvariable = False
                self.advance()
                return Token(LBRA, '{')
            
            if self.current_char == '}':
                isvariable = False
                self.advance()
                return Token(RBRA, '}')
            
            if self.current_char == ';':
                isvariable = False
                self.advance()
                return Token(SEMICOLON, ';')
            
            if isvariabale:
                token = self.var()
                if token in reserved:
                    if token == 'true':
                        return Token(TRUE, token)
                    if token == 'false':
                        return Token(FALSE, token)
                    if token == 'if':
                        return Token(IF, token)
                    if token == 'else':
                        return Token(ELSE, token)
                    if token == 'then':
                        return Token(THEN, token)
                    if token == 'while':
                        return Token(WHILE, token)
                    if token == 'do':
                        return Token(DO, token)
                    if token == 'skip':
                        return Token(SKIP, token)
                else:
                    return Token(VARIABLE, token)

            self.error()

        return Token(EOF, None)


# In[66]:


# A base node class called AST that other classes inherit from
class AST(object):
    pass

# A class to represent all binary operators (+,-,*)
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

# A class to hold an INTEGER token and the token’s value
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
class AssignOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right
        
class SkipOp(AST):
    def __init__(self, token):
        self.token = token
        
class WhileOp(AST):
    def __init__(self, op, condition, body):
        self.token = self.op = op
        self.condition = condition
        self.body = body
        
class IfOp(AST):
    def __init__(self, op, condition, true_body, false_body):
        self.token = self.op = op
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body
        
class ComSeqOp(AST):
    def __init__(self, left_com, op, right_com):
        self.token = self.op = op
        self.left_com = left_com
        self.right_com = right_com
        
class UnaryOp(AST):
    def __init__(self, op, right):
        self.token = self.op = op
        self.right = right

class TrueFalseOp(AST):
    def __init__(self, token):
        self.token = token
        
class VariableOp(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
        
# Parser
class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def Afactor(self):
        """Afactor : INTEGER | LPAREN Aexpr RPAREN """
        
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == VARIABLE:
            self.eat(VARIABLE)
            return VariableOp(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.Aexpr()
            self.eat(RPAREN)
            return node

    def Aterm(self):
        """term : factor MUL factor| factor AND factor"""
        node = self.Afactor()

        while self.current_token.type == MUL:
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)

            node = BinOp(left=node, op=token, right=self.Afactor())
        
        return node

    def Aexpr(self):
        """
        expr   : term PLUS term | term MINUS term 
    
        """
        node = self.Aterm()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.Aterm())

        return node
    
    def Bfactor(self):
        '''Bfactor : TRUE | FALSE | NOT Bfactor | (Bexpr) | Comp '''
        token = self.current_token
        if token.type == TRUE:
            self.eat(TRUE)
            return TrueFalseOp(token)
        elif token.type == FALSE:
            self.eat(FALSE)
            return TrueFalseOp(token)
        elif token.type == NOT:
            token = self.current_token
            self.eat(NOT)
            node = UnaryOp(op=token, right=self.Bfactor())
            return node
        else:
            temp_pos = self.lexer.pos
            try:
                node = self.Comp()
            except:
                node = None
            if node == None:
                self.lexer.pos = temp_pos
                self.lexer.current_char = self.lexer.text[temp_pos]
                self.current_token = token
                if token.type == LPAREN:
                    self.eat(LPAREN)
                    node = self.Bexpr()
                    self.eat(RPAREN)
            return node
        
    def Comp(self):
        """Comp : Bfactor EQUAL Bfactor| Bfactor LESS Bfactor"""
        node = self.Aexpr()
        token = self.current_token
        if token.type == EQUAL:
            self.eat(EQUAL)
        elif token.type == LESS:
            self.eat(LESS)
        elif token.type == MORE:
            self.eat(MORE)

        node = BinOp(left=node, op=token, right=self.Aexpr())

        return node
    
    def Bexpr(self):
        """
        Bexpr   : Bfactor AND Bfactor | Bfactor OR Bfactor
        
        """
        node = self.Bfactor()

        while self.current_token.type in (AND, OR):
            token = self.current_token
            if token.type == AND:
                self.eat(AND)
            elif token.type == OR:
                self.eat(OR)

            node = BinOp(left=node, op=token, right=self.Bfactor())

        return node
    
    def Cterm(self):
        
        '''Cterm :  { Cexpr } |
                    WHILE Bexpr DO Cexpr |
                    IF Bexpr THEN Cexpr ELSE Cexpr |
                    VARIABLE ASSIGNMENT Aexpr |
                    SKIP
        '''
        
        token_1 = self.current_token
        if token_1.type == WHILE:
            self.eat(WHILE)
            node = self.Bexpr()
            token_2 = self.current_token
            if token_2.type == DO:
                self.eat(DO)
                node = WhileOp(op=token_1, condition=node, body=self.Cterm())
            
                return node

        elif token_1.type == IF:
            self.eat(IF)
            node_1 = self.Bexpr()
            token_2 = self.current_token
            if token_2.type == THEN:
                self.eat(THEN)
                node_2 = self.Cexpr()
                token_3 = self.current_token
                if token_3.type == ELSE:
                    self.eat(ELSE)
                    node = IfOp(op=token_1, condition=node_1, true_body=node_2, false_body=self.Cterm())
                    return node
        
        elif token_1.type == VARIABLE:
            self.eat(VARIABLE)
            token_2 = self.current_token
            if token_2.type == ASSIGNMENT:
                self.eat(ASSIGNMENT)
                node = AssignOp(left=VariableOp(token_1), op=token_2, right=self.Aexpr())
                return node
            
        elif token_1.type == SKIP:
            self.eat(SKIP)
            node = SkipOp(token=token_1)
            
            return node
            
        elif token_1.type == LBRA:
            self.eat(LBRA)
            node = self.Cexpr()
            self.eat(RBRA)
        
            return node
    
    def Cexpr(self):
        ''' Cexpr : Cterm SEMICOLON Cterm '''
        
        node = self.Cterm()
        while self.current_token.type == SEMICOLON:
            token = self.current_token
            self.eat(SEMICOLON)
            
            node = ComSeqOp(left_com=node, op=token, right_com=self.Cterm())
        return node
    
    def parse(self):
        return self.Cexpr()


# In[67]:


# This class visits and interprets the nodes of the AST

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        #print(type(node).__name__)
        raise Exception('No visit_{} method'.format(type(node).__name__))

# Interpreter 
class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.current_vars = {}
    
    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == AND:
            return self.visit(node.left) & self.visit(node.right)
        elif node.op.type == OR:
            return self.visit(node.left) | self.visit(node.right)
        elif node.op.type == EQUAL:
            return (self.visit(node.left) == self.visit(node.right))
        elif node.op.type == LESS:
            return (self.visit(node.left) < self.visit(node.right))
        elif node.op.type == MORE:
            return (self.visit(node.left) > self.visit(node.right))
    
    def visit_UnaryOp(self, node):
        if node.op.type == NOT:
            return not self.visit(node.right)
        
    def visit_AssignOp(self, node):
        if node.op.type == ASSIGNMENT:
            self.current_vars[node.left.value] = self.visit(node.right)
            
    def visit_IfOp(self, node):
        if node.op.type == IF:
            if self.visit(node.condition):
                self.visit(node.true_body)
            else:
                self.visit(node.false_body)
    
    def visit_WhileOp(self, node):
        if node.op.type == WHILE:
            while self.visit(node.condition):
                self.visit(node.body)
                
    def visit_SkipOp(self, node):
        if node.token.type == SKIP:
            pass
                
    def visit_ComSeqOp(self, node):
        if node.op.type == SEMICOLON:
            self.visit(node.left_com)
            self.visit(node.right_com)
            
    def visit_VariableOp(self, node):
        if node.token.type == VARIABLE:
            if node.value in self.current_vars:
                return self.current_vars[node.value]
            else:
                return 0
    
    def visit_TrueFalseOp(self, node):
        if node.token.type == TRUE:
            return True
        if node.token.type == FALSE:
            return False
        
    def visit_Num(self, node):
        return node.value
    
    # interpreter in the form of a function called eval
    def eval(self):
        tree = self.parser.parse()
        return self.visit(tree)


# In[81]:


def main():
    
    try:
        text = input()
    except TypeError:
        raise("Only arithmatic, command and boolean expression is allowed.")
    

    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.eval()
    string = '{'
    first = True
    for key in sorted(interpreter.current_vars.keys()):
        if first:
            first = False
        else:
            string += ', '
        string += key + ' → '+str(interpreter.current_vars[key])
    string += '}'
    print(string)

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




