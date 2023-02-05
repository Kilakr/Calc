a = input()
result = compile(a, 'string', 'eval')
print(eval(result))