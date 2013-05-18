
def foo_while(arg)
	numbers = []
	for i in (0..arg)
		puts "At the top i is #{i}"
		numbers.push(i)
	
		puts "Numbers now: #{numbers}"
		puts "At the bottom i is #{i}"
	end
	return numbers
end

puts "The numbers: "

for num in foo_while(6)
	puts num
end
