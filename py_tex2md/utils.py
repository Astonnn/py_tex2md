import re


def escape(texstr):
    pass


def readEnv(file, env):
    content = file.read(1)
    while not content.endswith('\\end{' + env + '}'):
        content += file.read(1)
    end = '\\\\end\{' + env + '\}'
    # print(content)
    # print(end)
    print(re.sub(end, '', content))
    return re.sub(end, '', content)


def handleTitle(title):  # 处理多级标题
    list = ["part", "chapter", "section", "subsection", "subsubsection", "paragraph", "subparagraph"]
    def readtitle(str):
        tit = ""
        j = 0
        while str[j] != '{':
            j += 1
        while str[j + 1] != '}':
            j += 1
            tit += str[j]
        return tit

    for i in range(7):
        par = '\\\\' + list[i] + "\{.*\}"
        if re.match(par, title) is not None:
            if i == 0:
                return "<h1 style=\"font-size: bigger;\">"+readtitle(title)+"</h1>"
            else:
                return "<h"+str(i)+">"+readtitle(title)+"</h"+str(i)+">"
    return title


def matchBrackets(str, brackets):
    # 排除非法输入
    # pass
    def pair(br):
        if br == '(':
            return ')'
        elif br == '{':
            return '}'
        elif br == '[':
            return ']'
        else:
            return ','

    tu = tuple(brackets)
    res = ()
    flag = False  # False:正常；True:匹配状态
    temp = ""
    p = ''  # 记录被匹配的括号
    i_s = 0
    while i_s < len(str):  # i_s 是str中字符的下标
        if flag:
            while str[i_s] != p:
                temp += str[i_s]
                i_s += 1
            res += temp,
            temp = ""
            flag = False
            # i_s += 1
        elif str[i_s] in tu and not flag:  #
            flag = True
            res += temp,
            temp = ""
            p = pair(str[i_s])
            if p == ',':
                flag = False
            # i_s += 1
            # continue
        else:
            temp += str[i_s]
            # continue
        if i_s == len(str) - 1:
            res += temp,
        i_s += 1
    return res


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
