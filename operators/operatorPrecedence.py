#which one gets evaluated first?

""" 
multiplication and addition have a higher precedence than 
addition and subtraction, unless parenthesis are included.
"""

def main():
	quiz = 5*25+14/2
	print(quiz)


if __name__ == "__main__":main()