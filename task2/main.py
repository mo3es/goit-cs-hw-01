import sys
import os
path = os.path.dirname(__file__)
path = os.path.join(path, 'programm_files')
sys.path.append(path)
import my_token
import my_lexer


def main():
    text = '2 + 3^2*(4-1)**3 / 3'
    lexer = my_lexer.Lexer(text)
    token = lexer.get_next_token()
    while token.token_type != my_token.MyTokenType.EOF:
        print(token)
        token = lexer.get_next_token()

if __name__ == "__main__":
    main()
