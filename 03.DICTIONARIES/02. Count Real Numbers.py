numbers_list = list(map(float, input().split(' ')))

numbers_dict = {item: numbers_list.count(item) for item in numbers_list}

for key,value in sorted(numbers_dict.items()):
	print(f"{key} -> {value} times")