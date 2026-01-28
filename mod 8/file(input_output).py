# file operations
# open, read and close

#f = open("mod 8/sample.txt", "w")
# data = f.read()
#print(f.readline())  # read one line of whole txt
# print(f.readlines())   # Reads all lines into a list
# print(data)   # type = str


f = open("mod 8/sample.txt", "w")

f.write(" overwritten concepts ")

f.close()  # must neccesary if file is open once.
