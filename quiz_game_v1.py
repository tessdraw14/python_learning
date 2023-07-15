intro = input("Hello! Do you want to play a game? ")
print ("Great! Answer the folowing quetions to win!")
result = 0

first = input("What is Teresa's full name? ")
if first.lower() == "maria teresa nogueira moura":
	print("Correct!")
	result = result + 1
else: 
	print("Incorrect!")

second = input("How many animals does Teresa have? ")
if second == "4":
	print("Very good!")
	result = result + 1
else: 
	print("You are wrong!")

third = input("Which country does Teresa wants to go on vacation? ")
if third.lower() == "italy":
	print("That is right!")
	result = result + 1
else: 
	print("Interresting, but no.")

fourth = input("What Teresa's favorite color? ")
if fourth.lower() == "purple":
	print("Great!")
	result = result + 1
else: 
	print("Close! But no.")

print('"Cidade dos ossos", Cassandra Clare ou "Fogo", Kristin Cashore')
fith = input("Which on is Teresa's favorite book? ")
if fith.lower() == "fogo":
	print("Amasing!")
	result = result + 1
else: 
	print("So close!")

sixty = input("Last one! Which is Teresa's artist talent? ")
if sixty.lower() == "painting" or sixty.lower() == "drawing":
	print("Yay! Great job!")
	result = result + 1
else: 
	print("What! As if!")


print("You have a score of " + str(result) + " that means...")

if result == 6:
	print("Congrats! You did so well! Teresa must like you very much!")
elif result >= 3:
	print("Very good! You and Teresa must be good friend")
else:
	print("You didn't know enouth :( You should spend more time with Teresa.")