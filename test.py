from py_tex2md.utils import matchBrackets

a, b = input().split()
c = matchBrackets(a, b)
print(c)
