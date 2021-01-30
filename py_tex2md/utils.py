import re


def escape(texstr):
    pass


def matchBrackets(str, brackets):
    # 排除非法输入
    # pass
    res = ()
    temp = ""
    flag = True
    count = 0
    for i in str:
        if i == brackets[0]:
            flag = False
            res = res + (temp,)
            temp = ""
        elif not flag and i == brackets[1]:
            flag = True
            res = res + (temp,)
            temp = ""
        else:
            temp += i
        count += 1
        if count == len(str):
            res = res + (temp,)
    return res


def readEnv(file, env):
    content = file.read(1)
    while not content.endswith('\\end{' + env + '}'):
        content += file.read(1)
    end = '\\\\end\{' + env + '\}'
    # print(content)
    # print(end)
    print(re.sub(end, '', content))
    return re.sub(end, '', content)


def readWord(file):
    letter = file.read(1)
    word = ''
    while letter.isalpha():
        word += letter
        letter = file.read(1)
        print(word)
    return word


def strreadfirst(str, s):
    if len(str) == 0:
        return ''
    ch = str[0]
    prefix = ''
    i = 0
    while not prefix.endswith(s) and i < len(str):
        prefix += ch
        i = i + 1
        ch = str[i]
    prefix = prefix.replace(s, '')
    print('prefix', prefix)
    return prefix


def strreadline(str):
    if len(str) == 0:
        return ''
    ch = str[0]
    line = ''
    i = 0
    while ch != '\n' and i < len(str):
        line += ch
        i = i + 1
        ch = str[i]
        # print(line)
    return line
