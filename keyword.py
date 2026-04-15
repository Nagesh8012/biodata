Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import keyword
dir(keyword)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlist)
35
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
keyword.iskeyword('word')
False
keyword.iskeyword('while')
True
keyword.iskeyword('mca')
False
int=6
for=9
SyntaxError: invalid syntax
help('false')

help('False')

help('None')

help('True')

help('and')

help('as')

help('assert')

help('async')

help('await')

help('break')

help('class')

help('continue')

help('def')

help('del')

help('elif')

help('else')

help('except')

help('finally')

help('for')

help('from')

help('global')

help('if')

>>> help('import')

>>> help('in')

>>> help('is')

>>> help('lambda')

>>> help('nonlocal')

>>> help('not')

>>> help('not')

>>> help('or')

>>> help('pass')

>>> 
================ RESTART: M:/Python/decimalToBinary.py ================
