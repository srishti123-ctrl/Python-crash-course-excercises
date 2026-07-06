bikes=["Honda","Pulsor","Yamaha","Suzuki"]
bikes[0]='Ducati'
print(bikes)#It is modified output
bikes.append("Honda")
print(bikes)#It is used for addition
bikes.insert(1,'Pulsor125')
print(bikes)#it is used for insertion at a fix position
del bikes[2]
print(bikes)#it is used for deletion of elements
popped_bike=bikes.pop()
print(bikes)
print(popped_bike)