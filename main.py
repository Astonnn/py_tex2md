from py_tex2md import *

def main():
    print ("__name__ :", __name__)
    tex2md.tex2md('test.tex', 'test.md')
    pass


if __name__ == '__main__':
    main()