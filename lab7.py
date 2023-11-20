a = [1, 2, 3]
b = [1, 2, 3]
c = b[:]


# a SyntaxError('invalid syntax', ('<string>', 1, 1, "<method-wrapper '__add__' of list object at 0x000002706905B140>", 1, 2))
# b SyntaxError('invalid syntax', ('<string>', 1, 1, "<method-wrapper '__add__' of list object at 0x0000027069076580>", 1, 2))
# c SyntaxError('invalid syntax', ('<string>', 1, 1, "<method-wrapper '__add__' of list object at 0x0000027069076580>", 1, 2))