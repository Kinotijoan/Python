NUMBER_SYSTEM = {
	'zero': 0,
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9,
	'ten': 10,
	'eleven': 11,
	'twelve': 12,
	'thirteen': 13,
	'fourteen': 14,
	'fifteen': 15,
	'sixteen': 16,
	'seventeen': 17,
	'eighteen': 18,
	'nineteen': 19,
	'twenty': 20,
	'thirty': 30,
	'forty': 40,
	'fifty': 50,
	'sixty': 60,
	'seventy': 70,
	'eighty': 80,
	'ninety': 90,
	'hundred': 100,
	'thousand': 1000,
	'million': 1000000
	}


def num_list_2_num_int(nums:list):
	num_list = []
	for num in nums:
		num_list.append(NUMBER_SYSTEM[num])
	if (len(num_list) == 4):
		return (num_list[0] * num_list[1] + num_list[2] + num_list[3])
	elif (len(num_list) == 3):
		return (num_list[0] * num_list[1] + num_list[2])
	elif (len(num_list) == 2):
		if 100 in num_list:
			return num_list[0] * num_list[1]
		else:
			return num_list[0] + num_list[1]
	else:
		return num_list[0]


def parse_int(num_str:str):
	num_str = num_str.replace('-', ' ').lower()
	if (num_str.isdigit()):
		return int(num_str)

	num_list = num_str.strip().split()
	
	clean_num_list = []

	for num in num_list:
		if num in NUMBER_SYSTEM:
			clean_num_list.append(num)

	if 'million' in clean_num_list:
		million_index = clean_num_list.index('million')
	else:
		million_index = -1
	if 'thousand' in clean_num_list:
		thousand_index = clean_num_list.index('thousand')
	else:
		thousand_index = -1
	
	num_int = 0

	if (len(clean_num_list) > 0):
		if (len(clean_num_list) == 1):
			num_int += NUMBER_SYSTEM[clean_num_list[0]]
		else:
			if (million_index > -1):
				mil_mult = num_list_2_num_int(clean_num_list[0:million_index])
				num_int += mil_mult * 1000000
			
			if (thousand_index > -1):
				if million_index > -1:
					thou_mult = num_list_2_num_int(clean_num_list[million_index+1:thousand_index])
				else:
					thou_mult = num_list_2_num_int(clean_num_list[0:thousand_index])
				num_int += thou_mult * 1000

			if thousand_index > -1 and thousand_index != len(clean_num_list)-1:
				hundreds = num_list_2_num_int(clean_num_list[thousand_index+1:])
			elif million_index > -1 and million_index != len(clean_num_list)-1:
				hundreds = num_list_2_num_int(clean_num_list[million_index+1:])
			elif thousand_index == -1 and million_index == -1:
				hundreds = num_list_2_num_int(clean_num_list)
			else:
				hundreds = 0
			num_int += hundreds

	return num_int