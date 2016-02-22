#game execution module
import map_one
import character




class Engine(object):
	def __init__(self, player_character, Map=None):
		self.player_character = player_character
		self.map = Map
		if self.map is None:
			print('problem')

	def play(self, starting_room):
		current_room = self.map.current_room(starting_room)
		
		while current_room is not None:
			current_room = self.map.current_room(current_room)	


		
		
		
		

the_engine = Engine(character.example_character, map_one.map_)
the_engine.play('bedroom')





#the_map = map_one.Map()
#print dir(the_map.rooms['bedroom'])




