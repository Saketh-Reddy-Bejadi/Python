from collections import Counter
def Ransom(magazine,ransomNote):
    count=Counter(magazine)
    for c in ransomNote:
        if c not in count: return False
        elif count[c]==1 : del count[c]
        else: count[c]-=1
    return True
ransomNote = "a"
magazine = "b"
print(Ransom(ransomNote,magazine))