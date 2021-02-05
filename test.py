from py_tex2md.utils import matchBrackets,readTitle
readTitle(input())

# a, b = input().split()
a, b = '12(1,2){qwqw(q,w){eerr}}aa', '(){}'
c = matchBrackets(a, b)
print(c)