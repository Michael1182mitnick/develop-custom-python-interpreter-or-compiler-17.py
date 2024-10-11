# Develop a Custom Python Interpreter or Compiler
# Create a basic interpreter or compiler for a custom programming language with its own syntax and grammar.
# Define Syntax for MiniLang
# Lexical Analysis (Tokenizer)
"""
Example MiniLang code:
let x = 5;
let y = x * 2 + 3;
print(y);

"""
import re

# Define the types of tokens in MiniLang
TOKEN_SPEC = [
    ('NUMBER',    r'\d+(\.\d*)?'),   # Integer or decimal number
    ('ASSIGN',    r'='),             # Assignment operator
    ('PLUS',      r'\+'),            # Plus operator
    ('MINUS',     r'-'),             # Minus operator
    ('TIMES',     r'\*'),            # Multiplication operator
    ('DIVIDE',    r'/'),             # Division operator
    ('LPAREN',    r'\('),            # Left parenthesis
    ('RPAREN',    r'\)'),            # Right parenthesis
    ('SEMICOLON', r';'),             # Statement terminator
    ('PRINT',     r'print'),         # Print keyword
    ('LET',       r'let'),           # Variable declaration
    ('ID',        r'[a-zA-Z_]\w*'),  # Identifiers (variables)
    ('SKIP',      r'[ \t]+'),        # Skip spaces and tabs
    ('NEWLINE',   r'\n'),            # Line breaks
    ('MISMATCH',  r'.'),             # Any other character
]

# Compile the regular expressions for tokenization
token_re = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPEC)


def tokenize(code):
    tokens = []
    for match in re.finditer(token_re, code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' or kind == 'PRINT' or kind == 'LET':
            pass
        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character {value}')
        tokens.append((kind, value))
    return tokens


# Example usage
code = """
let x = 5;
let y = x * 2 + 3;
print(y);
"""

print(tokenize(code))
