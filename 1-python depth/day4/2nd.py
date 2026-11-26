# 1   Print 1 to N
n=10
for i in range(1,n+1):
    print(i) 
	
# 2	Sum of first N numbers
n=7
sum=0 
for i in range(1,n+1):
    sum+=i
print(sum)	
# 3	Sum of digits
a=123
sum=0
while a>0:
    rem=a%10
    sum+=rem
    a=a//10	
print(sum)
# 4	Reverse a number
a=123
rev=0
while a>0:
    rem=a%10
    a=a//10
    rev=(rev*10)+rem
print(rev)
# 5	Palindrome number	
a=565
temp=a
rev=0
while a>0:
    rem=a%10
    a=a//10
    rev=(rev*10)+rem
print(temp==rev)
# 6	Factorial	
fact=1
n=5
for i in range(1,n+1):
    fact=fact*i
print(fact)
# 7	Prime number	
n=11
if(n<=1):print("not prime")
elif n==2:print("prime")
elif(n%2==0):print("not prime")
for i in range(3,n):
      if i * i > n:
        break
      if(n%i==0):
        print("not prime")
        break
else:
    print("prime")
# 8	Multiplication table	
n=9
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
# 9	Print even numbers 
n=18
for i in range(1,n+1):
    if i%2==0:
        print(i)
# 10	Star patternsa
n=5
for i in range(0,5):
    for j in range(i+1):
        print("*",end="")
    print()