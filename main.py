# This a Python Mini Project
# To-Do List App(File-Based)
# Add task
# View Task
# Save Task
# Load Task from file
# See last updated time and date
# Final Features Test
import datetime
import os

x = datetime.datetime.now()


# ************** functions Zone **************
# Remove existing file
def removeExistingFile(name):
    os.remove(name)


# ************** functions Zone End **********
class ToDoList:
    def __init__(self):
        self.filename = "To-Do_List"

    # Methods

    # View Task
    # Usage: open and read the file content
    def readFile(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            print(f.read())

    # Add Task
    # Usage:Write a new line of task
    def addNewLine(self):
        task = input("Enter new task: ")
        with open(self.filename, 'a', encoding="utf-8") as f:
            f.write("- " + task + "\n")
        self.readFile()

    # Clear file contents
    def clearFile(self):
        with open(self.filename, 'w', encoding="utf-8") as f:
            # Display the time and date of the latest update
            f.write("Last Updated: " + x.strftime("%x") + " " + x.strftime("%X") + "\n")
            f.write(self.filename + "\n")  # The Heading
            self.readFile()

    # Input Match Case
    def inputMatchCase(self, value):
        match value:
            case 1:
                self.readFile()
            case 2:
                self.addNewLine()
            case 3:
                self.clearFile()
            case _:
                print("Oops! Wrong selection")

    # Display file menu
    def displayFileMenu(self):
        print("1 - View Tasks")
        print("2 - Add Task")
        print("3 - Clear file")
        userinput = int(input(": "))
        self.inputMatchCase(userinput)

    # Check File Existence
    # Usage: if file doesn't exist ,New file will be created
    def CheckFileExistence(self):
        try:
            open("To-Do_List", 'x', encoding="utf-8")
            with open("To-Do_List", 'w', encoding="utf-8") as f:
                # Display the time and date of the latest update
                f.write("Last Updated: " + x.strftime("%x") + " " + x.strftime("%X") + "\n")
                f.write("To-Do_List" + ":\n")  # The Heading
        except FileExistsError:
            self.displayFileMenu()


# Test Zone
f1 = ToDoList()
f1.CheckFileExistence()
