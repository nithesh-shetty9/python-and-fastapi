#while loop
i=0
while i!=5 and i!=-5:
     i-=1      #++i and --i are not valid it considers +(+i) and +(-i)
     print(i)
#for loop;
n=5
for i in range(5):
    print(i)
for i in range(1,5):
    print(i) 
for i in range(1,6,2):
    print(i)


#iterating over elements
num=[4,5,6,7,7]
for n in num:
    print(n)
#enumerate
for index,value in enumerate(num):
    print(index,value)

#break and conitineu same mechanims


#loop with else block which is feature in python helps execting the block of code when loop completed normally without break

