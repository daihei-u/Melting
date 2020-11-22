import math

print("1 0\n2 1")
iio=2
ii=1
for i in range(5000000):
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
    if(k==0):
        print( ii,ii-iio )
        iio=ii
print("\n")
