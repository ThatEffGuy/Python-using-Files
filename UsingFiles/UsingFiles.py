#opening a text file called "myText.txt" 
#and writing data to the file

with open("myText.txt","w") as f:
	f.write("this is the first line\n")
	f.write("this is the second line\n")
	f.write("this is the third line" + "\n")

#close file
print("Open the project folder to view the file")
input("\nPress Enter to Continue")

#writing numbers to a file
print("\nWriting numbers to a text file.  Text files can only contain text")
with open("myNumbers.txt","w") as f:
    f.write(str(5) +"\n")   #numbers converted to string before writing
    f.write(str(6) +"\n")
    f.write(str(56) +"\n")
#close file
print("Open the project folder to view the file")
input("\nPress Enter to Continue")

#example For Loop 
print("\nInputting marks into a text file using a FOR loop")
mark = 0
counter = 0
with open("marks.txt","w") as f:
	for counter in range (3):
		mark = int(input("Enter  a Mark : "))
		f.write(str(mark)+"\n")
	#end for
#end with close file
print("Open the project folder to view the file")
input("\nPress Enter to Continue")

#using a While loop to add data
print("\nInputting marks into a text file using a WHILE loop")
mark = 0
counter = 0
yesNo = ""

with open("marks.txt","w") as f:
    yesNo = input("Enter a Number [y/n] ")
    
    while yesNo =="y":
        mark = int(input("Enter  a Mark : "))
        f.write(str(mark)+"\n")
        yesNo = input("Enter a Number [y/n] ")
    #end while
#end with close file

#writing a number list to a text file
print("\nWriting a number list to a file")

myList = [1,2,3,4,5,6,7,89,34]

with open("output.txt","w") as f:
    for item in myList:
        f.write(str(item) + "\n")   # write string
    #end for
#end with
