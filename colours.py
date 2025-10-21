clrs=[]
count=int(input("Enter the number of colours :"))
print("Enter the colors :")
for x in range(count):
    color=input()
    clrs.append(color)
print("first color:",clrs[0],"last color:",clrs[count-1]) 
