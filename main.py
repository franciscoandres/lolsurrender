# LOL Surrender at 20 shit

players_votes = ["y", "y", "y", "y", "n"]
yes, no = 0, 0

yes = players_votes.count("y")
no  = players_votes.count("n")

if yes == 3 and no == 2:
	print("Not surrender because Rito pls... 3 IS GREATER THAN 2")
elif yes > no:
	print("Surrender")
elif yes == no:
	print("Not surrender")
else:
	print("Not surrender")

print(yes, no)
