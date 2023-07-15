import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
	top_of_range = int(top_of_range)

	if top_of_range <= 0:
		print("Please type a number larger then 0 next time.")
		quit()
else:
	print("Please type a number next time.")
	quit()

random_number = random.randint(0, top_of_range)
number_of_tries = 1

while True:
	user_guess = input("Make a guess: ")

	if user_guess.isdigit():
		user_guess = int(user_guess)
	else:
		print("Please type a number next time.")
		continue 
		
	if random_number == int(user_guess):
		print("You got it on your " + str(number_of_tries) + " try!")
		quit()

	elif random_number < int(user_guess):
		print("Try a smaller number next time.")
	
	else:
		print("Try a bigger number next time.")
			
	number_of_tries = number_of_tries + 1
 





