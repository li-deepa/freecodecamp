# title - uppercase of start letter in a word
#strip-strip the space
#lstrip-strip the left space
#rstrip-strip the right space
#upper-uppercase and lower-lowercase
# f is the format in python formats the return statement
#len-length of the word
#/t and /n to print in next line or tab space
# replace replaces the oldname with newname
#we can concatenate the strings by using +
first_name="ram"
last_name="gorrela"
fullname=f"{first_name}{last_name}"
print("hello"+fullname)
print(len(fullname))
print("hello"+"\t"+fullname)#prints output with a tabspace 
#between hello and fullname
print("hello"+"\n"+fullname)#print the output in 2 lines
print("hello:"+"\n\t"+fullname)
print(first_name.replace("ram","ravan"))
first_name="ravan"
first_name="ram"
print(first_name)
fullname=first_name+last_name
print(fullname)
