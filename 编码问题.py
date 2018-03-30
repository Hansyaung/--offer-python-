'''
假定一种编码的编码范围是a ~ y的25个字母，
从1位到4位的编码，如果我们把该编码按字典序排序，
形成一个数组如下： 
a, aa, aaa, aaaa, aaab, aaac, … …, 
b, ba, baa, baaa, baab, baac … …, 
yyyw, yyyx, yyyy 
其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 
编写一个函数，输入是任意一个编码，输出这个编码对应的Index.
'''

import sys
chars = 'abcdefghijklmnopqrstuvwxy'
char2num = {}
count = 0
for c in chars:
    char2num[c] = count
    count += 1
     
base4 = 1
base3 = 25 * base4 + 1
base2 = 25 * base3 + 1
base1 = 25 * base2 + 1
base = [base1,base2,base3,base4]
 
try:
    while True:
        s = sys.stdin.readline().strip()
        #print(s)
        if s == '':
            break
 
        ret = 0
        for i in range(len(s)):
            #print(s[i])
            num = char2num[s[i]]
            #print(num)
            ret += base[i]*num + 1
            #print(ret)
        print(ret-1)
except:
    pass
