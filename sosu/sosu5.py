#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
pint(2)
for wararerukazu in range(3,1000001,2):
  flg=1
  max_w=int(math.sqrt(wararerukazu))
  for warukazu in range(３,max_w+1,2):
    a=wararerukazu % warukazu
    if 0==a:
      flg=0
      break
  if 1==flg:
    print(wararerukazu)
