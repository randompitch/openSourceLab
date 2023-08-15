#Q8 Write a program to print each line of a file in reverse order.
file1 = open('myfile.txt', 'r')

while True:
	line = file1.readline()
	if not line:
		break
	print(line.strip()[::-1])

file1.close()
