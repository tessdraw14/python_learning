questions = [
	"What is Teresa's full name?",
	"How many animals does Teresa have?",
	"Which country does Teresa wants to go on vacation?",
	"What Teresa's favorite color?",
	"\"Cidade dos ossos\", Cassandra Clare ou \"Fogo\", Kristin Cashore'\n Which on is Teresa\'s favorite book?",
	"Last one! Which is Teresa's artist talent?"
]

replies = [
	"maria teresa nogueira moura",
	"4",
	"italy",
	"purple",
	"fogo",
	"drawing"
]

points = 0

for i in range(len(questions)):
	reply = input(questions[i])
	if replies[i] == reply:
		print("Correct!")
		points = points + 1
	else:
		print("Incorrect")

print("Correct answers: " + str(points))
