#occurance
string=input("Please enter your own word:")
char=input("Enter char:")
i=0
count=0

while(i<len(string)):
    if (string[i]==char):
        count=count+1
    i=i+1

print("The total number of Times",char,"has occured=",count)

#prime numbers
l=int(input("Enter a lower range:"))
u=int(input("Enter a upper range:"))
print("Prime numbers between",l,"and",u,"are:")

for num in range(l,u+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)

#product of mid digits
num=int(input("Enter a number:"))
t=num
numLen=0

while t>0:
    numLen=numLen+1
    t=int(t/10)
#mid digit
if numLen>=4:
    numLen=int(numLen/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numLen:
            midOne=rem
        elif chk==(numLen-1):
            midTwo=rem
        num=int(num/10)
        chk=chk+1
    prod=midOne*midTwo
    print("\nProduct of Mid digits",str(midOne),"*",str(midTwo),"is",prod)

else:
    print("It is not a 4 or more digit number!")