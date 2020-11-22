#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
keyin=int(sys.argv[1])
print(2)
for wararerukazu in range(3,keyin+1,2):
  flg=1
  max_w=int(math.sqrt(wararerukazu))
  for warukazu in range(3,max_w+1,2):
    a=wararerukazu % warukazu
    if 0==a:
      flg=0
      break
  if 1==flg:
    print(wararerukazu)
