class Surrender(object):
	def __init__(self, votes = None):
		self.votes = votes
		self.agree = 0
		self.disagree = 0

	def __minimum_votes(self):
		if not len(self.votes) <= 4:
			return False
		return True

	def __handle_votes(self):
		self.agree = votes.count("Y")
		self.disagree = votes.count("N")

	def __not_majority(self):
		return self.agree == 3 and self.disagree == 2

	def __draw(self):
		return self.agree == self.disagree

	def __majority(self):
		return self.agree > self.disagree

	def lets_do_it(self):
		self.__handle_votes()
		if self.__minimum_votes():
			print("Not enough votes")
		elif self.__not_majority():
			print("Not surrender")
		elif self.__majority():
			print("Surrender")
		elif self.__draw():
			print("Not surrender")
		else:
			print("Continue playing...")
		
votes = ["Y", "Y", "Y", "N", "N"]
surrender = Surrender(votes)
surrender.lets_do_it()