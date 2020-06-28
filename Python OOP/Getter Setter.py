class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor

	@property
	def info(self):
		return "name {} : \n\thealth: {}".format(self.name,self.__health)

	@property
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self, input):
		self.__armor = input

	@armor.deleter
	def armor(self):
		print('Armor is destroyed')
		self.__armor = None

ironman = Hero('Ironman',100,10)

print('merubah info')
print(ironman.info)
ironman.name = 'Tony Stark'
print(ironman.info)

print('getter dan setter untuk __armor:')
print(ironman.armor)
ironman.armor = 50
print(ironman.armor)

print('delete armor')
del ironman.armor
# use magic method dict
print(ironman.__dict__)
