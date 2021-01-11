
from . import utils
import re
import math

row_spacing = 30

def parse(pic_code):
    # 读取到\begin{picture}后调用，pic_code类型为文件
    mdstr = ''
    try:
        picstr = utils.readEnv(pic_code, 'picture')
        print('picstr', picstr)
        line = utils.strreadline(picstr)
        picstr = picstr.replace(line + '\n', '', 1)
        # print('picstr', picstr)
        width = 0
        height = 0
        print('line', line)
        if re.match('^(\(\d+,\d+\))', line):
            # width and height
            wnh = re.split('(\(|,|\))', line)
            print('width and height', wnh)
            width = int(wnh[2])
            height = int(wnh[4])
            mdstr += '<svg width="' + str(width) + '" height="' + str(height * 2 + row_spacing / 2) + '">\n'
            print(22, 'mdstr', mdstr)
            # 调整一波
        elif re.match('^(\(\d+,\d+\)){2}\s', line):
            # 暂时不用
            pass
        # print(re.match('^(\(\d+,\d+\)){1,2}\s', picstr))
        # print(re.sub('^(\(\d+,\d+\)){1,2}\s', '', picstr))
        while line != '':
            line = utils.strreadline(picstr)
            picstr = picstr.replace(line + '\n', '', 1)
            print(29, 'picstr', picstr)
            if line.startswith('\\put'):
                line = line.replace('\\put', '', 1)
                startcoord = utils.strreadfirst(line, '{')
                startxy = re.split('(\(|,|\))', startcoord)
                x = int(startxy[2])
                y = int(startxy[4])
                line = line.replace(startcoord, '', 1)
                line = line[1:len(line)-1]
                print('startcoord', startcoord)
                print('line', line)
                if line.startswith('\\line'):
                    # print('lllllllllllllll')
                    line = line.replace('\\line', '', 1)
                    endcoord = utils.strreadfirst(line, '{')
                    line = line.replace(endcoord, '', 1)
                    print(endcoord, line)
                    endxy = re.split('(\(|,|\))', endcoord)
                    dx = int(endxy[2])
                    dy = int(endxy[4])
                    times = int(line[1:len(line)-1])
                    theta = math.atan2(-dy, dx) * 180 / math.pi
                    print('x', x, 'y', y, 'dx', dx, 'dy', dy, times, theta)
                    mdstr += '\t<rect x="' + str(x) + '" y="' + str(height + row_spacing / 2 - y) + '" width="' + str(math.sqrt(dx * times * dx * times + dy * times * dy * times) ) + '" height="1" transform="rotate(' + str(theta) + ' ' + str(x) + ',' + str(y) + ')"/>\n'
                    print(57, 'mdstr', mdstr)
                elif line.startswith('\\circle'):
                    line = line.replace('\\circle', '', 1)
                    fill = False
                    if line[0] == '*':
                        fill = True
                        line = line.replace('*', '', 1)
                    # print(line[1:len(line)-1])
                    radius = int(line[1:len(line)-1])
                    mdstr += '\t<circle cx="' + str(x) + '" cy="' + str(height + row_spacing / 2 - y) + '" r="' + str(radius) + '"'
                    if not fill:
                        mdstr += ' stroke="currentColor" fill="none"'
                    mdstr += '/>\n'
                    print('circleline', line)
                    print(54, 'mdstr', mdstr)
                elif line.startswith('\\makebox'):
                    # 简单版本
                    line = line.replace('\\makebox', '', 1)
                    offsetcoord = utils.strreadfirst(line, '{')
                    line = line.replace(offsetcoord, '', 1)
                    offsetxy = re.split('(\(|,|\))', offsetcoord)
                    dx = int(offsetxy[2])
                    dy = int(offsetxy[4])
                    text = line[1:len(line)-1]
                    text = text.replace('$', '', text.count('$'))
                    print(line)
                    mdstr += '\t<text x="' + str(x + dx - len(text) * 6) + '" y="' + str(height + row_spacing / 2 - y - dy) + '">' + text + '</text>\n'
                    print('circleline', line)
            print('finalpicstr', picstr, '\n-----------------------------\n')
        mdstr += '</svg>\n'
        print(mdstr)
    except BaseException as e:
        print(e)
    finally:
        return mdstr
# if __name__ == '__main__':
#     str = "\\begin{picture}(10,80)(10,80)\n\\put"
#     print(str)
#     parse(str)