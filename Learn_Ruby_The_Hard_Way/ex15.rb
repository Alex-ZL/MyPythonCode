#get filename from the first argument
filename = ARGV.first

prompt = "> "
#open the file
txt = File.open(filename)

puts "Here's your file: #{filename}"
#print the file content
puts txt.read()

puts "I'll also ask you to type it again:"
print prompt
#get the filename from STDIN
file_again = STDIN.gets.chomp()

#open the file whose name is from STDIN
txt_again = File.open(file_again)

#print the file content
puts txt_again.read()
