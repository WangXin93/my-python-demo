def bubble(l):
	while True:
		count = 0
		for i in range(len(l)-1):
			if l[i] > l[i+1]:
				temp = l[i]
				l[i] = l[i+1]
				l[i+1] = temp
				count += 1
		if count == 0: 
			break

def select(lst):
    for i in range(len(lst)-1):
        _min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[_min]:
                _min = j
        lst[i], lst[_min] = lst[_min], lst[i]
	
