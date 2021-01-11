
from . import picture
from . import utils
def begin(tex, env):
    if env == 'picture':
        return picture.parse(tex)
    else:
        pass
class tex2md(object):
    """
    docstring
    """
    def __init__(self):
        pass
    def tex2md(texname, mdname):
        try:
            tex = open(texname)
            # print(tex.readline())
            md = open(mdname, "w")
            # lines = tex.readlines()
            # for line in lines:
            str = ''
            ch = tex.read(1)
            while ch != '':
                if ch == '\\':
                    command = utils.readWord(tex)
                # if str.startswith('\\begin{'):
                    if command == 'begin':
                        env = utils.readWord(tex)
                        md.write(begin(tex, env))
                        
                else:
                    str += ch
                    md.write(ch)
                ch = tex.read(1)
                print('str', str)
            # md.write(str)


            # print(tex.readline())

        except BaseException as e:
            print(e)
        finally:
            pass
if __name__ == '__main__':
    
    opentex('test.tex')