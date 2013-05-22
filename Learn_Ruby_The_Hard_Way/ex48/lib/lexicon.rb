Pair = Struct.new(:token, :word)

class Lexicon
	def initialize()
		@direction = ["north", "south", "east", "west", "down", "up",
			"left", "right", "back"]
		@verb = ["go", "stop", "kill", "eat"]
		@stop = ["the", "in", "of", "from", "at", "it"]
		@noun = ["door", "bear", "princess", "cabinet"]
	end

	def scan(arg)
		words = arg.split(" ")
		sentence = []
		words.each do |i|
			if @direction.include?(i)
				i = Pair.new(:direction, i)
				sentence.push(i)
			elsif @verb.include?(i)
				i = Pair.new(:verb, i)
				sentence.push(i)
			elsif @stop.include?(i)
				i = Pair.new(:stop, i)
				sentence.push(i)
			elsif @noun.include?(i)
				i = Pair.new(:noun, i)
				sentence.push(i)
			else
				begin
					i = Integer(i)
					sentence.push(Pair.new(:number, i))
				rescue
					i = Pair.new(:error, i)
					sentence.push(i)
				end
			end
		end
		return sentence
	end
end
