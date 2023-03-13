'''
APQR
ABQR
ABCR
ABCD
'''

a="ABCD"
b="PQR"
for i in range(4):
    for j in range(3):
        print(a[0:i+1],end="")
        print(b[i:j+3],end="")
        break
    print()