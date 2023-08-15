#Q6 Compute the number of characters, words and lines in a file.
with open("myfile.txt", 'r') as file1:
    nchar,nword,nlines = 0,0,0
    for line in file1:
        nlines += 1
        nchar += len(line)
        words = line.split()
        nword = len(words)
    print("Character count:", nchar)
    print("Word count:", nword)
    print("Line count:", nlines)