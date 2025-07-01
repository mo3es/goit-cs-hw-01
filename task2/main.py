import sys
import os

path_to_program_files = os.path.join(os.path.dirname(__file__), 'program_files')
sys.path.append(path_to_program_files)

import my_lexer 
import my_parser
import my_interpreter


def main():

    while True:

        try:
            text = input('Enter expression (or enter "exit" to quit): ')

            if text.lower() == 'exit':
                print("The programm was finished by user`s request")
                break

            lexer = my_lexer.Lexer(text)
            parser = my_parser.MyParser(lexer)
            tree_root = parser.parse()
            parser.print_parsing_tree(tree_root)
            interpreter = my_interpreter.MyInterpreter(tree_root)
            result = interpreter.interpret()
            print(result)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()