#game execution module
import inspect
import re
import sys
import map_one

rooms = {}
for name, type_ in inspect.getmembers(map_one, inspect.isclass):
		print name
		# key_name = name
		# pattern = re.compile(r'([a-z]{1}(?=[A-Z]{1}))(\w)')
		# key_name = pattern.sub(r"\1_\2", key_name)
		# key_name = key_name.lower()
		# rooms[key_name] = getattr(map_one, name)()


class Map(object):
	def __init__(self):
		self.rooms = rooms
		#self.rooms['bedroom'] = map_one.Bedroom()

	def current_room(self):
		#make this a recursive function...
		pass


class Engine(object):
	def __init__(self, Map=None):
		self.map = Map
		if self.map is None:
			print('problem')



	def play(self):
		pass


the_engine = Engine()
the_engine.play()

the_map = Map()
print(the_map.rooms)
test = the_map.rooms['bedroom']
print(test.enter())


#test = getattr(map_one, 'Bedroom')
#print(type(test()))
