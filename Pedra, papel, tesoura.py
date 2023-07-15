import random 

computer_wins = 0
user_wins = 0

options = ["pedra", "papel", "tesoura"]

while True:
	user_pick = input("Escolhe Pedra, Papel, Tesoura ou P para parar: ")
	user_pick = user_pick.lower()
	if user_pick == "p":
			print("Tu: ", user_wins, "  Adversário: ", computer_wins, )
			quit()

	if user_pick not in options:
		print("Plesase type one of the options.")
		continue

	random_number = random.randint(0, 2)
	computer_pick = options[random_number]	
	print ("O adversário escolheu", computer_pick, ".")


	if user_pick == "pedra" and computer_pick == "tesoura":
		print("Venceste!")
		user_wins = user_wins + 1

	elif user_pick == "papel" and computer_pick == "pedra":
		print("Venceste!")
		user_wins = user_wins + 1

	elif user_pick == "tesoura" and computer_pick == "papel":
		print("Venceste!")
		user_wins = user_wins + 1

	elif user_pick == computer_pick:
		print("Empataste.")

	else:
		print("Perdeste.")
		computer_wins = computer_wins + 1
