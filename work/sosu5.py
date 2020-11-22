import sys
import math
if len(sys.argv)>1:
  keyin=int(sys.argv[1])
else:
  keyin=100
print(2)
ii=1
for wararerukazu in range(3,keyin+1,2):
  flg=1
  max_w=int(math.sqrt(wararerukazu))
  for warukazu in range(3,max_w+1,2):
    a=wararerukazu % warukazu
    if 0==a:
      flg=0
      break
  if 1==flg:
    ii=ii+1
    print(wararerukazu)

print("num : ",ii)
