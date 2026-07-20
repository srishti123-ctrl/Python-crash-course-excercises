for value in range(1, 20):#counting 1 to 20 using for loop
    print(value)
numbers= []
for value in range(1,10000000):
    number=value
    numbers.append(number)
    print(f"The number is :{numbers}")

print(min(numbers))
print(max(numbers))
print(sum(numbers))    
odd_number=list(range(1,21,2))
print(f"The odd number is :{odd_number}")
multiples_of_Three=[]
for value in range(1,20):
    three=value*3
    multiples_of_Three.append(three)
print(multiples_of_Three)
cubes=[]
for value in range(1,11):
    cube=value**3
    cubes.append(cube)
print(cubes)    
cubes=[value**2 for value in range(1,11)]
print(cubes)