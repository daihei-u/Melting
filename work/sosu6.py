import sys
import math
#--- sub ---
def sosu(n):
    flg=1
    max_w=int(math.sqrt(n))
    for warukazu in range(3,max_w+1,2):
        a=n % warukazu
        if 0==a:
            flg=0
            break
    return flg

#--- main ---
if len(sys.argv)>1:
  keyin=int(sys.argv[1])
else:
  keyin=100
print(2)
ii=1
for wararerukazu in range(3,keyin+1,2):
    if sosu(wararerukazu):
        ii=ii+1
        print(wararerukazu)

print("ii : ",ii)
