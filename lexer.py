import re
import os

class token:
  def __init__(self):
    name = ''
    value = ''
    line = 0
    char = 0


def lexer(path):

  STRUCTURE_TOKENS = {
    '\n'  :   '<NEW_LINE>',
    '\t'  :   '<TAB>',
    '*'   :   '<ITEM>'
  }

  with open(path) as mydata:
      data = mydata.read()

  lexemes = []

  current_lexeme = []
  current_line = 1;

  for i, c in enumerate(data):

    if i == 0 and c in STRUCTURE_TOKENS:
      lexemes.append(STRUCTURE_TOKENS[c])
    elif c in STRUCTURE_TOKENS:
      if current_lexeme != []:
        lexemes.append(''.join(current_lexeme).strip())
        current_lexeme = []
      lexemes.append(STRUCTURE_TOKENS[c])
    else:
      current_lexeme.append(c)

    current_line = current_line + 1 if c == '\n' else current_line

  return lexemes

lexemes = lexer('test_files\\folderstruct1.txt')
print(lexemes)
lexemes = lexer('test_files\\folderstruct2.txt')
print(lexemes)
lexemes = lexer('test_files\\folderstruct3.txt')
print(lexemes)