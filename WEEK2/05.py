#Q5 Use Python Built-in Functions 'open', 'read', 'readline', 'write', 'writeline' to work with files.
file1 = open("myfile.txt","w")
L = ["I am Megha. \n","I am in Batch B15 \n","I am doing OpenSourceSoftwareLab work. \n"]

file1.write("Hello \n") 
file1.writelines(L)
file1.close() 

file1 = open("myfile.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()
file1.seek(0)

print( "Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
