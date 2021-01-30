from . import picture
from . import utils

import re


def begin(tex, env):
    if env == 'picture':
        return picture.parse1(tex)
    elif env == 'document':
        pass
    else:
        pass
settings = {
    'half_row_spacing': 15
}
# def comment(mdstr, texstr):
#     partition = texstr.partition('\n')
#     # html 注释
#     mdstr += '<!--' + partition[0] + '-->\n'
#     # ; 注释
#     mdstr += '\n;' + partition[0] + '\n'
#     # : 注释
#     mdstr += '\n:' + partition[0] + '\n'
#     # 解析法注释
#     mdstr += '[comment]: <> (' + partition[0] + ')\n'
#     mdstr += '[//]: # (' + partition[0] + ')\n'
#     texstr = partition[2]

class tex2md(object):
    """
    docstring
    """

    def __init__(self):
        pass
    def convert(texstr):
        mdstr = ''
        try:
            while len(texstr) > 0:
                partition = texstr.partition('\\')
                # 无法解析注释% {}
                print(partition)
                mdstr += partition[0]
                cmdmatch = re.match(r'([a-zA-Z]+|[\(\)\{\}#$%&\\]|[_~^]\{\})(.*)', partition[2], re.S)
                # print(type(cmdmatch))
                print(cmdmatch)
                if cmdmatch is None:
                    print('None, Unknown Command')
                    mdstr += tex2md.convert(partition[2])
                    break
                command = cmdmatch.group(1)
                texstr = cmdmatch.group(2)
                # remains = partition[2][cmdmatch.span()[1]:len(partition[2])]
                print(command, texstr)
                # print(command.group(0))
                if command == 'begin':
                    envmatch = re.match(r'\{([a-zA-Z]+)\}(.*)', texstr, re.S)
                    if envmatch is None:
                        print('None, Unknown Environment')
                        break
                    env = envmatch.group(1)
                    texstr = envmatch.group(2)
                    partition = texstr.partition('\end{' + env + '}')
                    texstr = partition[2]
                    if env == 'picture':
                        picstr = partition[0]
                        partition = picstr.partition(')')
                        sizematch = re.match(r'[ ]*\([ ]*([\d\.]+)[ ]*,[ ]*([\d\.]+)', partition[0], re.S)
                        width = float(sizematch.group(1))
                        height = float(sizematch.group(2))
                        mdstr += '<svg width="' + str(width) + '" height="' + str(height * 2 + settings['half_row_spacing']) + '">'
                        mdstr += tex2md.convert(partition[2])
                        mdstr += '</svg>'
                    elif env == 'document':
                        pass
                    elif env == 'equation':
                        mdstr += '$$\n' + partition[0] + '\n$$'
                    elif env == 'enumerate':
                        pass
                    else:
                        pass
                    print('132', env, texstr)
                elif command in '{}#$%&':
                    mdstr += command
                elif command == '\\':
                    mdstr += '\n'
                elif command == '(' or command == ')':
                    mdstr += '$'
                elif command == '_{}':
                    mdstr += '_'
                elif command == '~{}':
                    mdstr += '~'
                elif command == '^{}':
                    mdstr += '^'
                elif command == 'textbackslash':
                    mdstr += '\\'
                elif command == 'put' or command == 'makebox':
                    # matchBrackets
                    putmatch = utils.matchBrackets(texstr, '(){}')
                    # putmatch = re.match(r'\(([\d\.]+),([\d\.]+)\)(.*)', texstr, re.S)
                    partition = putmatch[1].partition(',')
                    dx = float(partition[0])
                    dy = float(partition[2])
                    mdstr += '<g transform="translate(' + str(dx) + ' ' + str(dy) + ')">'
                    mdstr += tex2md.convert(putmatch[2])
                    mdstr += '</g>'
                    texstr = putmatch[3]
                elif command == 'line':
                    pass
                elif command == 'circle':
                    # print('circle', texstr)
                    circlematch = re.match(r'\*?\{([\d\.]+)\}(.*)', texstr, re.S)
                    radius = float(circlematch.group(1))
                    mdstr += '<circle r="' + str(radius) + '"'
                    if texstr.startswith('*'):
                        mdstr += ' stroke="currentColor" fill="none"'
                    mdstr += '/>'
                    texstr = circlematch.group(2)
                else:
                    pass
                    # texstr = partition[2]
        except BaseException as e:
            print(e)
        finally:
            return mdstr
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


# if __name__ == '__main__':

#     opentex('test.tex')


if __name__ == '__main__':
    opentex('test.tex')
