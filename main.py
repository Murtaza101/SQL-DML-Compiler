import lexer


def main():
    # reading the contents of the source code
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()

    #
    # Lexer
    #

    # calling the lexer class and initialize with the source code
    lex = lexer.Lexer(content)
    # we now call the tokenize method
    tokens = lex.tokenize()


main()