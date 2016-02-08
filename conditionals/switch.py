#a python switch statement:

def main():
	choices = dict(
		one = 'Joe',
		two  = 'Ann',
		three = 'Gaz',
		four = 'Elvis',
		five = 'Irene'
		)
	x = 'eight'
	#use get method which returns a default value
	# get method is of type dectionary
	print(choices.get(x, 'gerrarrahia!'))


if __name__ == "__main__": main()	
