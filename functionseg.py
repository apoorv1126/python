#multiple parameter example)
def profile(name, *age):
	print name
	print age
	
profile('apoorv',2,3,4,5)

#multiple dictionary using function
 
def car(**item):
	print item
 	
 	
car(apple=4, mango=6)

#more example of above two

def prof(name,surname,*age,**item):
	print name, surname
	print age
	print item
	
print "enter name:"
var1=raw_input()
print "surname name:"
var2=raw_input()
print "ages"
var3=input()
print "items"
var4=raw_input()

prof(var1, var2, var3, var4)



