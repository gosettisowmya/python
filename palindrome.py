n=int(input("enter a number:"))
pal=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(pal==rev):
    print("palindrome number:")
else:
    print("not a palindrome number")
