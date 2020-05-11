#Jordan Goodman
#4/25/17
#goodmanJordanA8.py
#using functions to edit lists from text files
   
def toDolist(mainSelection, readFile):   
    lines = readFile.readlines()
    readFile.close()
    newList = [i.rstrip('\n') for i in lines]
    #this strips \n from i and adds i in lines to the new list 'newList'
    printChoices()
    selectChoice = int(input("Enter the number of your selection: "))
    print()
    if selectChoice >=1 and selectChoice <=5:
        selection(selectChoice, newList, mainSelection)

def mainChoices():#I used this function to make my code appear cleaner and save space
    print("\nWelcome to your to-do list! \n")
    print("Select a list: \n 1. Weekly \n 2. Monthly \n 3. Yearly goals \n", end=' ')
    print("4. Summer programming list \n 0. To quit the program")
    print()
def printChoices():
    print("\n Select an option for your list: \n \n 1. Add an item to the list")
    print(" 2. Remove an item from the list \n 3. Print the list \n 4. Save the", end=' ')
    print("list and return to the main list menu")
    print(" 5. Return to the main list menu without saving \n ")
def selection(choiceSelection, newList, lists):
    #choiceSelection is the 1-5 selection for the list
    #newList is the list made with the toDolist function
    #lists is for choice 4 to know which file to edit
    count = 0
    while choiceSelection >=1 and choiceSelection <=3:
        if choiceSelection == 1:
            item = input("\nenter a new item for the list: ")
            newList.append(item)
            print("item succesfully added. Your new list:\n")
        elif choiceSelection == 2:
            item = input("\nenter the item you would like removed from the list: ")
            print()
            if item in newList:
                newList.remove(item)
                print("item succesfully removed. Your new list:\n")
            else:
                print("the item you remove must be in the list")
        #no need for elif ~~~ 3 because the list is already going to print    
        for x in newList:#instead of putting this for loop at the end of
            print(x)     #each if statement I added it here
        print()
        printChoices()
        choiceSelection = int(input("Enter the number of your selection: "))

    if choiceSelection == 4:#this is outside of the loop because these 2 selections
        if lists == 1:      #take you back to the main function
            savedFile = open("weeklytodo.txt","w")
        elif lists == 2:
            savedFile = open("monthlytodo.txt","w")
        elif lists == 3:
            savedFile = open("yearlytodolist.txt","w")
        elif lists == 4:
            savedFile = open("programmingtodo.txt","w")
        for lines in newList:
            savedFile.write(lines)
            #i used the write \n so that each list item would be on its own line
            savedFile.write('\n')
        savedFile.close()
        main()
    elif choiceSelection == 5:
        main()
        
def main():
    mainChoices()
    selection = int(input("Enter the number of your selection(0 to quit): "))
    if selection != 0 and selection >= 1 and selection <=4:
#I openend the file for reading here and added it to the toDolist function
        if selection == 1:
            readFile = open("weeklytodo.txt", "r")
            toDolist(selection, readFile)
        elif selection == 2:
            readFile = open("monthlytodo.txt", "r")
            toDolist(selection, readFile)
        elif selection == 3:
            readFile = open("yearlytodolist.txt", "r")
            toDolist(selection, readFile)
        elif selection == 4:
            readFile = open("programmingtodo.txt", "r")
            toDolist(selection, readFile)


main()
print("Thanks for using my to-do list function")

            
