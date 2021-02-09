from py_tex2md import *


def main():
    print("__name__ :", __name__)
    # tex2md.tex2md('test.tex', 'test.md')
    ttt = '''
\\tableofcontents{}
%zxasdasd
aa%zcccccc
\\begin{picture}(80,10)
\put(20,0){\circle{3}}
\put(60,0){\circle*{3}}
\put(0,0){\line(1,0){80}}
\put(0,0){\line(1,1){80}}
\put(20,8){\makebox(0,0){O}}
\put(60,8){\makebox(0,0){A}}
\end{picture}
\part{part}\chapter{chapter}
'''
    print('!!!!!\n', tex2md.convert(ttt))
    # print('!!!!!!!!!!!!!!!!!!!!\n', tex2md.convert('$A$'))
    pass


if __name__ == '__main__':
    main()