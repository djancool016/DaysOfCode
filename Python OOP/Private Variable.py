class Hero:

	# class variabel
	jumlah = 0
	__privateJumlah = 0

	def __init__(self,name,health):
		self._name = name
		self.health = health

		# variabel instance private
		self.__private = "private"
		# variabel instance protected
		self._protected = "protected"


lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)

#error saat mengakses atribut __private
#print(Hero.__private)

#walaupun private, namun tetap dapat diakses dan diubah diluar class dengan obj._cls__attribute
print(lina._Hero__private)

lina._Hero__private = "Ubah Private Variable"
print(lina._Hero__private)


