asking = True

while asking:

	answer = input("How are you? Please type how you feel or 'Q' to quit: ")

	

	if answer.lower() == "great" or answer.lower() == "q" or answer.lower() == "good":

		asking = False

	else:

		print("That's not what I'm asking for...")



print("Thank you")