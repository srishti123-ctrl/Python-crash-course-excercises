invitation=["Gita","Elina","Dipin"]
print(f" Hello {invitation[0].title()}, You are invited in my  dinner party.")
print(f"Hello {invitation[1].title()}, You are invited in my dinner party.")
print(f"Hello {invitation[2].title()}, You are invited in my dinner party.")
print(f"I heard you are not available for my dinner party and it's okay. Next time we will meet {invitation[2].title()}. Don\'t worry.. ")
print("There is another person who is available. So i will call the next person")
print("Hello! Samir, You said you are available for tommorow dinner. You are invited in my tomorrow dinner party.")
invitation[2]='Samir'
print(invitation)
print("Hey Guys! ,I have found a bigger dinner table. Now i can add more people as more people are waiting for my dinner invitation. So, I am calling more people in tommoreow dinner.")
invitation.insert(0, "Riya")
invitation.insert(2, "Sid")
invitation.insert(5,"Ram")
print(invitation)
print("Guys, the bigger dinning table is not available in time . There is only teo seats are available in current dinning table")
notavailable=invitation.pop(5)
print(f"Sorry {notavailable.title()}, There is not available space in dinning table for you")
notavailable=invitation.pop(4)
print(f"Sorry {notavailable.title()}, There is not available space in dinning table for you")
notavailable=invitation.pop(3)
print(f"Sorry {notavailable.title()}, There is not available space in dinning table for you")
notavailable=invitation.pop(2)
print(f"Sorry {notavailable.title()}, There is not available space in dinning table for you")
print(f" Hello {invitation[0].title()}, You are invited in my  dinner party.")
print(f" Hello {invitation[1].title()}, You are invited in my  dinner party.")
print(invitation)
del invitation
invitation.clear()
print(invitation)





