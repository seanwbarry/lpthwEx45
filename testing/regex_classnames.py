## getting regex of class names to work


#print(re.search('(?<=abc)def', 'abcdef'))
#print(re.search('(?<=-)\w+', name))

#print(re.sub(name, ([a-z]{1}[A-Z]{1})/$1-$2))

#print rooms

def replace_lower(match):
	return match.group(1).lower()

print('-'*20)

mystring = 'asdfAsdf'
pattern = re.compile(r'([a-z]{1}(?=[A-Z]{1}))(\w)')
newstring = pattern.sub(r"\1-\2", mystring)
print(newstring)

print('-'*20)

mystring = 'asdf_Asdf'

pattern = re.compile(r'(_(?=[A-Z]{1}))(\w)')

newstring = re.sub(r'([A-Z]){1}', replace_lower, mystring)
print(newstring)


s = 'start TT end'
callback = lambda pat: pat.group(1).lower()
asdf = re.sub(r'([A-Z]){2}', lambda pat: pat.group(1).lower(), s)
print asdf



##########
#one solution
#print(mystring.lower())
##########

#print(pattern.__dir__())
##print(pattern.group(0))
##print(pattern.group(1))
##newstring = pattern.sub(r"\1", lambda second: second.groups(1).lower(), mystring)
#print(newstring)

# print(dir(pattern))
# print(pattern.__getattribute__)



# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)

# print(dir(m))


rooms = {}
for name, type_ in inspect.getmembers(map_one, inspect.isclass):
		key_name = name
		pattern = re.compile(r'([a-z]{1}(?=[A-Z]{1}))(\w)')
		key_name = pattern.sub(r"\1_\2", key_name)
		key_name = key_name.lower()
		rooms[name] = name()
		#print(type(name))



rooms = {}
for name, type_ in inspect.getmembers(map_one, inspect.isclass):
		print name
		# key_name = name
		# pattern = re.compile(r'([a-z]{1}(?=[A-Z]{1}))(\w)')
		# key_name = pattern.sub(r"\1_\2", key_name)
		# key_name = key_name.lower()
		# rooms[key_name] = getattr(map_one, name)()