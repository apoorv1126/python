#Tuples example - Tuples cant be changed like list once you defined it
var1="hello %s, how are %s"
tuple_eg=('apoorv','you')
print `var1%tuple_eg`
print `var1.find('how')` #gives index number of how, where it starts

#if else exaples

fish=raw_input()
colour='blue'
if fish == "tuna":
	print "this is your fish"
elif fish=="salmon":
	print 'this is not your fish'
else:
	print 'unknown'
	
#"is" is a operator which give true if and only if both are exactly equal
check='tuna'

print `fish is check`
