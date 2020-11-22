#!/usr/bin/env python
# -*- coding: utf-8 -*-



import math


def chksym(sosu,flgSosu,debug):
    # example sosu=11
    # (0) 1 2 3 4 5 6 7 8 9 a b  number a=10,b=11
    # (0) 1 1 1 0 1 0 1 0 0 0 1  flgSosu index=number, no shift
    #                         1 0 0 0 1 0 1 0 1 1 1 (0)
    # x                     1 0 0 0 1 0 1 0 1 1 1 (0)
    #                     1 0 0 0 1 0 1 0 1 1 1 (0)
    # x                 1 0 0 0 1 0 1 0 1 1 1 (0)
    #                 1 0 0 0 1 0 1 0 1 1 1 (0)
    # x             1 0 0 0 1 0 1 0 1 1 1 (0)
    #             1 0 0 0 1 0 1 0 1 1 1 (0)
    # x         1 0 0 0 1 0 1 0 1 1 1 (0)
    #         1 0 0 0 1 0 1 0 1 1 1 (0)         Hit Loop 1
    # x     1 0 0 0 1 0 1 0 1 1 1 (0)           x
    #     1 0 0 0 1 0 1 0 1 1 1 (0)             loop 2

    if 1==debug:
        print("chksym -- in",sosu,"-",flgSosu)
    half=int((sosu-1)/2)
    mid=half+1
    result=""
    flg=0
    #print("chksym -- mid",mid,"   half" ,half)
    # find start point : start last 2nd sosu.
    for i in range(sosu-1,0,-1):
        if 1==flgSosu[i]:
            hit=i
            #print("chksym -- found hit",hit)
            break;

    #compare flgSosu
    for i in range(hit,mid-1,-1):
        sum=0
        check=[]
        #print("chksym -- check range i:from",hit,"to >0   j:from 0 to <",half)
        for j in range(sosu-i):
            if 1==debug:
                print("chksym --",i,j,"-- val",i+j+1,"<->",i-j-1,"======  flg",flgSosu[i+j+1],"<->",flgSosu[i-j+1])
            if flgSosu[i+j+1]==flgSosu[i-j-1]:
                check.append(flgSosu[i+j+1])
                sum=sum+flgSosu[i+j+1]
            else:
                check.append(0)

        #print("chksym --sum:",sum)
        if 0<sum:
            result=str(i)
            for j in range(sosu-i):
                if 1==check[j]:
                    result=str(i-j-1)+","+result+","+str(i+j+1)
            flg=1
            #print("chksym -- result:",result,flg)
            break;
        else:
            flg=0


    if 1==debug:
        print("chksym --chk cancel mid",i,flgSosu[i],sum,"--result",result)
        print("chksym flgSosu :",flgSosu)
    if (0==flgSosu[i]) & (1==sum):
        #print("chksym --cancel mid",i,flgSosu[i],sum,"--result",result)
        flg=0
        result=""
    #print("chksym -- return:",result,flg)
    return(flg,result)


def main():
    debug=0
    sosu=[2,3]
    chkSosu=[0,1,2,3]
    flgSosu=[0,1,1,1]
    mid={}
    #print("- 1 0\n- 2 1")
    print("found Sosu 3 sym 1,2,3")
    iio=3
    for ii in range(5,1000,2 ):
        k=0
        ii2=int(math.sqrt(ii))
        #print ("------root ii2",ii2)
        for jj in range(3,ii2+1,2):
            #print("------mod(",ii,",",jj,")=",ii%jj,"- root",ii2)
            if(0==ii%jj):
                k=1
                break
        #ii is sosu
        if(k==0):
            sosu.append(ii)
            chkSosu.append(ii)
            flgSosu.append(0)
            flgSosu.append(1)
            #print( "-",ii,ii-iio )
            iio=ii
            half=int((ii-1)/2)
            mid0=ii-half
            check=[]
            ans=""
            flg=0
            #print("-- sosu=",ii,"half=",half,"mid=",mid0)
            if 61==ii:
                debug=1
            else:
                debug=0
            [flg,ans]=chksym(ii,flgSosu,debug)
            if(1==flg):
                print("found Sosu",ii,"sym", ans)
            else:
                print("not found!!!",ii,ans)
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
