def talk(animal_type, name)
	if animal_type == 'bird'
		return "#{name} says Chirp Chirp!"
	elsif animal_type == 'dog'
		return "#{name} says Bark Bark!"
	elsif animal_type =='cat'
		return "#{name} says Moew Moew"
	end
end

puts talk('cat', 'Ngân')
		
		