# LOL Surrender at 20 shit

players_votes = ["y", "y", "y", "y", "n"]
positive, negative = 0, 0

for vote in players_votes:
	if "y" in vote:
		positive += 1
	elif "n" in vote:
		negative += 1
	else:
		positive += 0
		negative += 0

if positive == 3 and negative == 2:
	print("Not surrender because Rito pls... 3 IS GREATER THAN 2")
elif positive > negative:
	print("Surrender")
elif positive == negative:
	print("Not surrender")
else:
	print("Not surrender")

print(positive, negative)
