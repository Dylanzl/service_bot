import print as pr

def init(parser):
    try:
        while True:
            l1 = f.readline().split(" ")
            if len(l1[0]) != 0:
                l1[1] = l1[1].replace("\n", "")
                parser[l1[0]] = l1[1]#将它们对应放入字典中
            else:
                break
        return parser
    except EOFError:
        pass

def isDigit(my_str):#判断是否为数字
    try:
        int(my_str)
    except ValueError:
        return False
    return True

def match(s):#判断是否与某个step匹配
    if s not in parser.keys():#没有直接匹配step成功
        for i in range(len(l1)):
            key = l1[i]#取出每个键看是否有与输入想重合的话语
            if s in key or key in s:#有与之相关step修改其为那个step
                s = key
                break
    return s

parser = {}
f = open('logicalscript1.txt', encoding='utf-8')
init(parser)#初始化parser
print("请问先生/女士怎么称呼")
str1 = input()
#查看用户是否来过
fp = open("username.txt", encoding='utf-8')
d = {}
l2 = []
i = 1
try:
    while True:
        l2 = fp.readline().split()
        if len(l2) != 0:
            d[l2[0]] = i
            i = i + 1
        else:
            break
except EOFError:
    pass
# print(d)

if str1 in d.keys():
    pr.print_a(str1)
    pr.print_ask()
else:#没来过加入username里面
    pr.print_hi(str1)
    pr.print_ask()
    out = open("username.txt", 'a', encoding='utf-8')
    out.write(str1)
    out.write(" ")
    out.write(str(i))
    out.write('\n')
    out.close()

l1 = []
for each in parser.keys(): #将字典中的键放入一个列表里面
    l1.append(each)
s = input()
while s != "结束对话" and s != "结束":
    s = match(s)#判断是否与某个step匹配
    while s in parser.keys() and isDigit(parser[s]):
        s = parser[s]
    if s in parser.keys():#第一次没有直接匹配，但是与其中的某个键有重合的话语
        print(parser[s]) #Speak
        if s == '97' or s == '98':#退货政策或者到货时间说完后结束当前话题
            print("请问还有什么可以让冰冰帮助到您的吗？")
            pr.print_ask()
    else:#都不存在于键中再次询问
        print("不好意思，冰冰可能有点笨，不知道您的真正需求，请问您能把问题描述的清楚一点吗？")
        pr.print_ask()
    s = input()
pr.print_bye(str1)
