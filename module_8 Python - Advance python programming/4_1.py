# Write a Python program to read the contents of a 
# file and print them on the console.
file=open("file1.txt","r")
content=file.read()
print(content)
file.close()