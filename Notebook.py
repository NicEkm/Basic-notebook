import time    # Needs to be imported and pip installed before running.
import pickle  #


def notebook(): # Defining main function.
    try: #
        file = input('Give name of the file: ') # Testing, if inputted file exists, and if not, creates it. Use .dat files, so they can be used by pickle module. For example (notebook.dat).
        open(file) #
    except: #
        IOError
        print('No such a file exists, creating file.', file) # If file is not found, create it.
        open(file,'w+') # Opens file.
		
    myList = [line.rstrip('\n') for line in open(file)] # Created myList to use and handle data in file.
	
    while True: # Created while-loop.
        print('(1) Read notebook\n(2) Add note\n(3) Edit note\n' # Program gives options that user can choose what to do.
              '(4) Delete note\n(5) Save & Quit') #
        a = int(input('What do you want to do?: ')) # Program asks user to choose from 1-5 and then do what user wants.
        if a == 1: # If user input is 1, porgram reads the notebook.
            for x in myList: # Reads every line of the file.
                print(x) #
        if a == 2: # If user input is 2, program opens file and then asks user to write new note.
            f = open(file, 'w') # Open file.
            b = (input('Write new note: ') + ' ::' + time.strftime("%X %x")) # Takes new note and add timestamp to it.
            myList.append(b) # Adds note to the [myList]
            f.close() # Closes file.
        if a == 3: # If user input is 3, program tells how many notes there are and asks user to choose which one of them they want to replace.
            print('There is ', len(myList), ' notes.') #
            replace = (int(input('Which one of them do you want to edit (''1'' is first)?: ')) - 1) # Takes user int(input) and reduce 1 of it, to get correct index number correlating right note.
            print(myList[replace]) # Prints the old note.
            newNote = input('Write new text: ') + ' ::' + time.strftime("%X %x") # Asks new note.
            myList[replace] = newNote # Replacing old note with new one.
        if a == 4: # If user input is 4, program tells how many notes there are and asks user to choose which one of them they want to delete.
            print('Tehere is ', len(myList), ' notes.') #
            delete = (int(input('Which one of them do you want to delete (''1'' is first)?: ')) - 1) # Takes user int(input) and reduce 1 of it, to get correct index number correlating right note.
            print('Deleting note ' + myList[delete]) # Printing the note, user is deleting.
            del myList[delete] # Deletes note from the [myList]
        if a == 5: # If user input is 5, program Saves and Quits, using pickle library, to encode the file.
            print('Saving..') # This is printed for the visualization to the user.
            f = open(file, 'wb') # Opens 'file', and pickle.dumbs [myList] to it.
            pickle.dump(myList, f) #
            break # Breaks the while-loop


if __name__== "__main__": 
    notebook()
