# LOL Surrender at 20 shit

players_votes = ["y", "y", "y", "y", "n"]
positive, negative = 0, 0

positive = players_votes.count("y")
negative = players_votes.count("n")

if positive == 3 and negative == 2:
	print("Not surrender because Rito pls... 3 IS GREATER THAN 2")
elif positive > negative:
	print("Surrender")
elif positive == negative:
	print("Not surrender")
else:
	print("Not surrender")

print(positive, negative)
