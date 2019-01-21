=begin
class Dog
	def talk
		puts "Bark!"
	end

	def move(destination)
		puts "Run on the #{destination}"
	end
end

fido = Dog.new
rex = Dog.new

fido.talk
fido.move('road')
=end
class Cat
	def initialize(name='Ngân', age='21')
		@name = name
		@age = age
	end

	def setName=(name)
		@name = name
	end

	def setAge=(age)
		@age = age
	end

	def getAge
		@age
	end

	def getName
		@name
	end

	def talk
		puts "#{@name} say Moew Moew"
	end

end

class Dog
	attr_accessor :name, :age
	def initialize(name = 'Nghị', age = 22)
		@name = name
		@age = age
	end
	def talk
		puts "#{@name} say Ủn Ỉn"
	end
end

rabbit = Cat.new()
dog = Dog.new()
puts dog.name
puts dog.age
dog.age = (21)
puts dog.age
dog.talk
rabbit.talk
puts(rabbit.getName)
puts(rabbit.getAge)
