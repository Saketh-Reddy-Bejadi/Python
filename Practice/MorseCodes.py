morseCode=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
n=int(input())
words=input().split()
letToM={}
for i in range(26):
    letter=chr(i+ord('a'))
    morse=morseCode[i]
    letToM[letter]=morse
tra=set()
for w in words:
    t=''
    for c in w:
        t+=''.join(letToM[c])
    tra.add(t)
print(len(tra))