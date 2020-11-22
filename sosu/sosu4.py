#!/usr/bin/env python
# coding: utf-8

for wararerukazu in range(2,1000001):
  flg=1
  for warukazu in range(2,wararerukazu):
    a=wararerukazu % warukazu
    if 0==a:
      flg=0
      break
  if 1==flg:
    print(wararerukazu)
