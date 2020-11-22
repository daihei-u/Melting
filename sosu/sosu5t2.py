#!/usr/bin/env python
# -*- coding: utf-8 -*-
print(2)
for wararerukazu in range(3,51,2):
  flg=1
  for warukazu in range(3,wararerukazu,2):
    a=wararerukazu % warukazu
    if 0==a:
      flg=0
      break
  if 1==flg:
    print(wararerukazu)
