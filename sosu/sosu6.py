#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys

keyin=int(sys.argv[1])

i=1
print(2)
for wararerukazu in range(3,keyin+1,2):
  flg=1
  max=int(math.sqrt(wararerukazu))
  for warukazu in range(2,max+1):
    a=wararerukazu % warukazu
    if 0==a:
      flg=0
      break

  if 1==flg:
    i=i+1
    print(wararerukazu)

print(i)
