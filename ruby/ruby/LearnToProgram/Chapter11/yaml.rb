require "yaml"
test_array = ['Give Quiche A Chance',
			  'Mutants Out!',
			  'Chameleonic Life-Forms, No Thanks']

test_string = test_array.to_yaml
file_name = 'RimmerTShirts.txt'

File.open(file_name, "w") do  |file| 
	file.write test_string
end

read_string = File.read file_name
read_array = YAML::load read_string

puts read_string

puts test_string

puts read_array

puts test_array
