# coding: utf-8
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

#---main---
keyin=int(input("調べたい数を入力してください  "))
if sosu(keyin):
    print(keyin,"は素数です")
else:
    print(keyin,"は素数ではありません")
