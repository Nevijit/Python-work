
asking = True
while asking:
	answer = input("How are you? Please type how you feel or 'Q' to quit: ")
	answer = answer.lower()
	
	if answer == "good" or answer == "q":
		asking = False
	else:
		answerlist = answer.split()
		print("we will now look at...")
		print(answerlist)
		print("...")
		new_answer = " "
		count = 1
		for item in answerlist: # for every 'item' that is inside 'answerlist'
			print()
			print("looking at word #" + str(count))
			#answernew=answer.replace("me","you")
			if item == "i":
				print("found a 'i', changing it to a 'you'")
				new_answer += " you "
			elif item == "me":
				print("found a 'me', changing it to a 'you'")
				new_answer += " you "
			elif item == "my":
				print("found a 'my', changing it to a 'your'")
				new_answer += " your "
			elif item == "am":
				print("found a 'am', changing it to a 'are'")
				new_answer += " are "
			else:
				print("this word isn't in a splitlist, so we just add it: " + item)
				new_answer += " " + item + "  "
				count += 1
			print(new_answer)
		#print(new_answer)
		#print("That's not what I'm asking for...please answer \"good or somthing else\"")
	print("Thank you")

