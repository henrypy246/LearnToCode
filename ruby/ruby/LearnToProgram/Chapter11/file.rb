file_name = 'listerQuote.txt'
test_string = 'I promise that I swear absolutely that ' +
				'I will never mention gazpacho soup again.'
File.open(file_name, "w") do  |io|  
	io.write test_string
end

read_string = File.read file_name
print read_string == test_string