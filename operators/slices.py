#slices


def main():

	list = []
	list = [1,2,3,4,5,6,7,8,9,10]
	print(list[5])
	print(list[5:8])

if __name__ == "__main__":main()	

""" 
A slice has 3 parts : the beginning, the end and the step;
list[27:43:3]...this basically prints out every element after
the 3rd step from 27 to 42.

A slice can also be used to assign values to specified elements;
list[27:43:3] = (99,99,99,99,99,99) 99 is assigned to all elements
gotten through condition 3


"""

