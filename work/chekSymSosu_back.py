#!/usr/bin/env python
# -*- coding: utf-8 -*-



import math

def main():
    sosu=[0,1,2]
    flgSosu=[0,1,1]
    mid={}
    print("- 1 0\n- 2 1")
    iio=2
    ii=1
    for i in range(10):
        k=0
        ii=ii+2
        ii2=int(math.sqrt(ii)/2)
        jj=1
        for j in range(ii2):
            jj=jj+2
            #print("------mod(",ii,",",jj,")=",ii%jj,"-",ii2,j,)
            if(ii%jj==0):
                k=1
                break
        #ii is sosu
        if(k==0):
            sosu.append(ii)
            flgSosu.append(0)
            flgSosu.append(1)
            print( "-",ii,ii-iio )
            iio=ii
            half=int((ii-1)/2)
            mid0=ii-half
            check=[]
            print("-- sosu=",ii,"half=",half,"mid=",mid0)
            for mm in range(half):
                print("mm",mm)
                mid=mid0+mm
                for kk in range(half-mm):
                    print("kk",kk,"mid+kk+1",mid+kk+1,"lenflgSosu",len(flgSosu))
                    if flgSosu[mid+kk+1]==flgSosu[mid-kk-1]:
                        check.append(flgSosu[mid+kk+1])
                    else:
                        check.append(0)
                sum=0
                l=0
                ans=""
                leftHalf=""
                rightHalf=""
                for x in check:
                    l=l+1
                    if x == 1:
                        leftHalf=str(mid-l)+","+leftHalf
                        rightHalf=rightHalf+","+str(mid+l)
                        sum=sum+x
                if sum==1:
                    if flgSosu[mid]==1:
                        ans=leftHalf+"("+str(mid)+")"+rightHalf
                        print("found",ans)
                    else:
                        print("not found!!")
                elif sum>1:
                    ans=leftHalf+"("+str(mid)+")"+rightHalf
                    print("found", ans)
                else:
                    print("not found!!!")
                    continue
        #ii is not sosu
        else:
            flgSosu.append(0)
            flgSosu.append(0)
    print("\n")
    for x in sosu:
        print(x)


if __name__ == '__main__':
    main()
