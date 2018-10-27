list = []
for x in range(1,11):
    list.append((lambda y: y**2)(x))
print (list)