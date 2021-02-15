'''a=5
add,sub,mul,div,rem,expo =0,0,0,1,1,1
add+=a #add=add+5 =0+5
print(add)
sub-=a
print(sub)
mul*=a
print(mul)
div /=a #div=div/5 =1/5
print(div)
rem %=a
print(rem)
expo **=a
print(expo)
'''
num=int(input("Enter a number :"))
if num%2 == 0:
    print("Given number",num, "is Even")
else:
    print("Given number",num,"is ODD ")
