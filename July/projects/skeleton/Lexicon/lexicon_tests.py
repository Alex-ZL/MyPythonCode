from nose.tools import *
from ex48 import lexicon, parser

def test_directions():
	assert_equal(lexicon.scan("North"), [('direction', 'north')])
	result = lexicon.scan("north sOuth east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')])
	result = lexicon.scan("go kill eat")
	assert_equal(result, [('verb', 'go'),
						  ('verb', 'kill'),
						  ('verb', 'eat')])

def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')])
	result = lexicon.scan("the in of")
	assert_equal(result, [('stop', 'the'),
						  ('stop', 'in'),
						  ('stop', 'of')])

def test_nouns():
	assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
	result = lexicon.scan("bear princess")
	assert_equal(result, [('noun', 'bear'),
						  ('noun', 'princess')])

def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("3 91234")
	assert_equal(result, [('number', 3),
						  ('number', 91234)])

def test_errors():
	assert_equal(lexicon.scan("WhatEver"), [('error', 'whatever')])
	result = lexicon.scan("bear IAS princess")
	assert_equal(result, [('noun', 'bear'),
						  ('error', 'ias'),
						  ('noun', 'princess')])

def test_peek():
	a_word_list = lexicon.scan("I can't live without you.")
	assert_equal(parser.peek(a_word_list), 'error')
	b_word_list = lexicon.scan("north will be you next aim.")
	assert_equal(parser.peek(b_word_list), 'direction')
	c_word_list = lexicon.scan("go forward, just like I did.")
	assert_equal(parser.peek(c_word_list), 'verb')
	d_word_list = lexicon.scan("bear will not bear everything.")
	assert_equal(parser.peek(d_word_list), 'noun')

def test_parse_verb():
	a_word_list = lexicon.scan("test some noun.")
	assert_raises(parser.ParserError, parser.parse_verb,a_word_list)
	b_word_list = lexicon.scan("kill me if I failed.")
	assert_equal(parser.parse_verb(b_word_list), ('verb','kill'))
	c_word_list = lexicon.scan("at kill world")
	assert_equal(parser.parse_verb(c_word_list), ('verb','kill'))

def test_parse_object():
	a_word_list = lexicon.scan("door some noun.")
	b_word_list = lexicon.scan("north me if I failed.")
	c_word_list = lexicon.scan("at kill world")
	assert_equal(parser.parse_object(a_word_list), ('noun','door'))
	assert_equal(parser.parse_object(b_word_list), ('direction','north'))
	assert_raises(parser.ParserError, parser.parse_object, c_word_list)

def test_parse_subject():
	a_word_list = lexicon.scan("eat it princess")
	test_subject = parser.parse_subject(a_word_list, ('noun','subj'))
	assert_equal(test_subject.verb, 'eat')
	assert_equal(test_subject.object, 'princess')
	assert_equal(test_subject.subject, 'subj')

def test_parse_sentence():
	a_word_list = lexicon.scan("it princess eat it")
	#a_test_sentence = parser.parse_sentence(a_word_list)
	assert_raises(parser.ParserError, parser.parse_sentence, a_word_list)
	b_word_list = lexicon.scan("eat princess")
	b_test_sentence = parser.parse_sentence(b_word_list)
	assert_equal(b_test_sentence.verb, 'eat')
	assert_equal(b_test_sentence.object, 'princess')
	assert_equal(b_test_sentence.subject, 'player')

	c_word_list = lexicon.scan("what is the matter?")
	assert_raises(parser.ParserError, parser.parse_sentence, c_word_list)
