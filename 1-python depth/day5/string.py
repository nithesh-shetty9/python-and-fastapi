name="nithesh"
language="python"
# print(name)

#index works same as arry 

#suports negative index;
print(name[-1])#h
print(name[::-1])#revere


#3)string slicing string[start:stop:step]//exclusive stop

print(name[0:3:2])
new_name=name[0:2]
print(new_name)


#imp in python strings are immuatable
n="python"
n="J"+n[1:]
print(n)


#string methods
text="Hello world"
print(text.upper())#upper
print(text.lower())#lower
print(text.capitalize())#frst letter capiaL
print(text.title())#first letter of a word is capial
print(text.swapcase());#swap


#removing whitespaces
t="    hi      "
print(t.strip())
print(t.lstrip())
print(t.rstrip())


#hadnling userinputs

te="I love js"
print(text.find("js"));
print(te.replace("js","ython"))
print(text.count("o"))#int
print(text.startswith())#bol
print(text.endswith())#bool


#split string to array;
#join array to strings