#how to define a set
st={} #using direct entering values olny
#print(type(st))

#we can create a empty set by using set()
st=set()
print(type(st))

#we can store same and different type of data
st={10,20,"sibin",True}
print(st)

#elemts in set are unique means that duplicate are not allowed
st={10,20,"sibin",True,10,20,"sibin",True}
print(st)

#insertion order is not preserved
st={10,20,"sibin",True}
print(st)

#we can't Using index value print
#print(st[2]) # this code canot work