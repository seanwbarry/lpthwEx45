#room module
import re

def replace_hypens_with_spaces(variable):
	if '_' in variable:
		variable = re.sub('_', ' ', variable)
		return variable
	else:
		return variable

def list_of_methods(self):
	room_activities = {}
	for method in dir(self):
		room_activity = return_methods(method)
		if room_activity is not None:
			room_activities[room_activity] = method
	return room_activities

def return_methods(method):
	if not method.startswith('enter') and not method.startswith('__'):	
		return replace_hypens_with_spaces(method)
	else:
		return None

def choice():
	choice = raw_input("> ")
	choice = re.sub(' ', '_', choice)
	return choice

class _BaseRoom(object):
	def __init__(self):
		pass

	def enter(self):
		print('-'*30)
		print('you are in the '+type(self).__name__)
		print('you can:')
		room_activities = list_of_methods(self)
		for activity in room_activities:
			print activity
		print('go to other room')
		print('what do you want to do?')
		user_choice = choice()
		return user_choice, room_activities

class Bedroom(_BaseRoom):
	def __init__(self):
		pass

	def sleep(self):
		print('you did some sleeping')

	def waste_time(self):
		print('you wasted some time')

class DiningRoom(_BaseRoom):
	def __init__(self):
		pass

	def eat_food(self):
		pass

class TrainingRoom(_BaseRoom):
	def __init__(self):
		pass

	def train(self):
		pass

class CompetitionRoom(_BaseRoom):
	def __init__(self):
		pass

	def play_opponent(self):
		pass

class Map(object):
	def __init__(self):
		self.rooms = {
			'bedroom': Bedroom(),
			'dining_room': DiningRoom(),
			'training_room': TrainingRoom(),
			'competition_room': CompetitionRoom()
		}

	def current_room(self, room_name, user_choice=None, room_activities=None):
		#make this a recursive function...
		if user_choice is None:		
			user_choice, room_activities = self.rooms[room_name].enter()

		if user_choice in room_activities.values():
			getattr(self.rooms[room_name], user_choice)()
			self.current_room(room_name)

		elif user_choice == 'go_to_other_room':
			self.print_list_of_rooms()
			user_choice = choice()
			if user_choice in self.rooms:
				return user_choice
			else:
				print '-'*30
				print 'that is an incorrect choice, please try again'
				self.current_room(room_name, user_choice=user_choice, room_activities=room_activities)
		else:
			print '-'*30
			print 'that is an incorrect choice, please try again'
			self.current_room(room_name)
		
		# while user_choice is not None:
		# 	if user_choice in room_activities:
		# 		getattr(self.rooms[room_name], user_choice)()
		# 	elif user_choice in self.rooms:
		# 		return user_choice
	def go_to_other_room(self, next_room):
		pass		

	def print_list_of_rooms(self):
		print('which room would you like to go to?')
		for room in self.rooms:
			print replace_hypens_with_spaces(room)


map_ = Map()