def func(operation):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '**': lambda a, b: a ** b,
        '/': lambda a, b: a / b,
    }
    return operations[operation]


result = func('+')
print(result(1, 2))
