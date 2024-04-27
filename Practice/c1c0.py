grid=[["B","W","B"],["B","W","W"],["B","W","B"]]
m=0
for i in range(len(grid)):
    wc=grid[i].count('W')
    bc=grid[i].count('B')
    m=max(m,wc,bc)
if m>=3:
    print(True)
else:
    print(False)