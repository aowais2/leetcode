
# Online Python - IDE, Editor, Compiler, Interpreter

def triangle(num):
    space = ' '
    ast = '*'
    num_ast = 1
    num_space = num - 1
    for i in range(num):
        print(space * num_space , ast * num_ast , space * num_space)
        num_ast += 2
        num_space -= 1
        
triangle(5)
