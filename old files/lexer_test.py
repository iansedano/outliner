from lexing import lexer
import io
import sys

def foo(inStr):
    print ("hi"+inStr)

def test_foo():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.

    lexemes = lexer('test_files\\folderstruct1.txt')
    print_lex(lexemes)                              
    
    sys.stdout = sys.__stdout__                     # Reset redirect.
    print ('Captured', capturedOutput.getvalue())   # Now works as before.

    lexemes = lexer('test_files\\folderstruct1.txt')
    print_lex(lexemes)
    lexemes = lexer('test_files\\folderstruct2.txt')
    print_lex(lexemes)
    lexemes = lexer('test_files\\folderstruct3.txt')
    print_lex(lexemes)

test_foo()



class TestLexer(unittest.TestCase):
    """
    Our basic test class
    """

    def test_lex(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = lexer('test_files\\folderstruct1.txt')
        self.assertEqual(res, 120)


if __name__ == '__main__':
    unittest.main()


if __name__ == "__main__":
    lexemes = lexer('test_files\\folderstruct1.txt')
    print_lex(lexemes)
    lexemes = lexer('test_files\\folderstruct2.txt')
    print_lex(lexemes)
    lexemes = lexer('test_files\\folderstruct3.txt')
    print_lex(lexemes)