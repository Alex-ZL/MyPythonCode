from_file, to_file = ARGV
script = $0

puts "Copying from #{from_file} to #{to_file}"

indata = File.open(from_file).read()

puts "This input file is #{indata.length} bytes long"

puts "Does the output file exist? #{File.exist? to_file}"
puts "Ready, hit RETURN to continue, CTRL-C to abort."
STDIN.gets

output = File.open(to_file, 'w')
output.write(indata)

puts "Alright, all done."

output.close()
