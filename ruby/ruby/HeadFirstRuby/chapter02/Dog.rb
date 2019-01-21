class Dog
	attr_reader :name, :age
	def initialize(name = 'henry', age = 22)
		self.name = name
		self.age = age
	end

	def name=(name)
		if name == ''
			raise "Name can't be blank"
		else
			@name = name
		end
	end

	def age=(age)
		if age <= 0
			raise "age can't be nagative"
		else
			@age = age
		end
	end
end

#nick = Dog.new
nick = Dog.new('a',10)
puts nick.name
puts nick.age
puts nick.instance_variables
#nick.name = 'Nghị'
#nick.name = ''
