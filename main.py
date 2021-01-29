from py_tex2md import *

def main():
    print ("__name__ :", __name__)
    tex2md.tex2md('test.tex', 'test.md')
    ttt = \
    '''
    \\begin{picture}(80,10)
    \put(0,0){\line(1,0){80}}
    \put(20,0){\circle{3}}
    \put(60,0){\circle*{3}}
    \put(20,8){\makebox(0,0){$O$}}
    \put(60,8){\makebox(0,0){$A$}}
    \end{picture}
    \(\\begin{picture}(80,10)\n\put(0,0)\_{}
    '''
    print('!!!!!\n', tex2md.convert(ttt))
    pass


if __name__ == '__main__':
    main()