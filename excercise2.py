players=["hari","Ram","Sita","Gita","Gopal","Govinda"]
print(players[-3])
print("Here is the first  three elements of lists:\t")
print(players[:3])
print("Here is the middle elements of lists:")
print(players[2:4])
print("Here is the last three elements of lists:")
print(players[3:])
friend_pizzas=["Chicken pizza","Cheese Pizza","Pineapple Pizaz","Panner Pizza"]
your_pizza=friend_pizzas[:]
friend_pizzas.append("HOt pizza")
print(friend_pizzas)
your_pizza.append("Vegetable pizza")
print(your_pizza)
print("My favourite pizza are:")
for your_pizza in your_pizza:
    print(your_pizza)
print("My favourite pizza are:")
for friend_pizzas in friend_pizzas:
    print(friend_pizzas)

