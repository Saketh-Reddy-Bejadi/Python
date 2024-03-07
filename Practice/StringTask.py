chars=input()
chars=chars.lower()
for c in chars:
    if c in 'aeiouy' :
        chars=chars.replace(c,"")
chars="".join("."+m for m in chars)
print(chars.lower())             