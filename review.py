

def construct_zoo(dictionary_list):
	 dict = {}

	 for words in dictionary_list:
	 	for key, value in words.items():
	 		dict[key] = value
	 return dict



def extract_characters(list_strings):
	lst = []

	splat = list(list_strings)
	for words in splat:
		for element in words:
			lst.append(element)
	return lst


def is_int_or_string(mystery):
	
	if int == type(mystery):
		return "int"
	else:
		return "string"


# use a list comprehension!!!
def odd_numbers(array_numbers):
	
	return [ x for x in array_numbers if x % 2 != 0]


def long_words(words, minimum_length):

	lst = []
	
	for item in words:
		if len(item) > minimum_length:
			lst.append(item)
	return lst





