morseCode=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
n=int(input())
w=input().split()
letToM={}
for i in range(26):
    l=chr(i+ord('a'))
    m=morseCode[i]
    letToM[l]=m
tra=set()
for i in w:
    t=''
    for c in i:
        t+=''.join(letToM[c])
    tra.add(t)
print(len(tra))