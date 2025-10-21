n= int(input("ENTER NUMBER OF N TERMS:"))
a=0
b=1
print(f"first",n,"fibanacci number are")
for i in range(n):
    if i==0 or i==1:
        print(i)
    else:
        c=a+b
        a=b
        b=c
        print(c)
        
