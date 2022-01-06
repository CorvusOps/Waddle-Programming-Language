from interpreter.lexer import run
    
while True:
    text = input('waddle > ')
    result, error = run(text)

    if error: print(error.as_string())
    else: print(result)