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


def readTitle(title):  # 处理多级标题
    tar = ""
    if re.match('.*section\{.*', title) is None:
        return title
    else:
        i = 0
        sec = ""
        tit = ""
        while title[i] != '{':
            tit += title[i]
            i += 1
        i += 1
        while title[i] != '}':
            sec += title[i]
            i += 1
        # print(sec)
        n = tit.count("sub") + 1
        if n > 6:
            return title
        print("<h" + str(n) + ">" + sec + "</h" + str(n) + ">")
        return "<h" + str(n) + ">" + sec + "</h" + str(n) + ">"
    # pass


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
        if br == ')':
            return '('
        elif br == '}':
            return '{'
        elif br == ']':
            return '['
        else:
            return br
    res = []
    beg = 0
    # 截取子串begin
    i_s = 0
    # brackets index
    count = 0
    # 数数
    for c in range(len(str)):
        # print(i_s)
        if str[c] == brackets[i_s]:
            if count == 0:
                # brackets匹配成功
                i_s += 1
                res.append(str[beg:c])
                beg = c + 1
                if i_s >= len(brackets):
                    break
            else:
                count -= 1
        elif str[c] == pair(brackets[i_s]):
            count += 1
    res.append(str[beg:len(str)])
    # print(temp)
    # temp += c
    return tuple(res)

def _matchBrackets(str, brackets):
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
