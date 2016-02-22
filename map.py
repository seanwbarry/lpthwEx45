#room module
class BaseRoom(object):
	def __init__(self):
		pass

class Bedroom(BaseRoom):
	def __init__(self):
		print("you're in your bedroom")

	def sleep(self):
		pass

	def waste_time(self):
		pass

class DiningRoom(BaseRoom):
	def __init__(self):
		print("you're in the dining room")

	def eat_food(self):
		pass

class TrainingRoom(BaseRoom):
	def __init__(self):
		print("you're in the training room")

	def train(self):
		pass

class CompetitionRoom(BaseRoom):
	def __init__(self):
		print("you're in the competition room")

	def play_opponent(self):
		pass