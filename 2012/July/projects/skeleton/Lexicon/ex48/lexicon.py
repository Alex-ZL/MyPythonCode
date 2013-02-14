##lexicon script for exercise 48

# scanner to analyse lexicon
lexicon = {'north':'direction', 'south':'direction', 'east':'direction',
'west':'direction', 'down':'direction', 'up':'direction', 'left':'direction'
,'right':'direction', 'back':'direction', 'go':'verb', 'stop':'verb',
'kill':'verb', 'eat':'verb', 'the':'stop', 'in':'stop', 'of':'stop',
'from':'stop', 'at':'stop', 'it':'stop', 'door':'noun', 'bear':'noun',
'princess':'noun', 'cabinet':'noun'}

def scan(instr):
	inlist = instr.lower().split()
	outlist = []
	for item in inlist:
		if item.isdigit():
			outlist.append(('number', int(item)))
		else:
			outlist.append((lexicon.get(item,'error'), item))
	return outlist
