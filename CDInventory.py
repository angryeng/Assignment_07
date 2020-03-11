#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DOranski, 2020-Mar-02, Modified file TODOs
# DKlos, 2020-Mar-04, Refactoring add_entry and del_entry. try / except on read_file
# DOranski, 2020-Mar-09, Updating script for Module 7 with error handling.
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
table = [] # list to help manage data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    # def add_entry():
    def add_entry(cd_id, cd_title, cd_artist, table):
        """Function to manage the addition of entries to the existing table
       
        Adds entries to the existing table after the user uses the 'a' functionality
        built into the script.
       
        Args:
            cd_id: the integer ID of the CD
            cd_title: the title of the CD
            cd_artist: the CD artist's name
           
        Returns:
            None
       
        """
        # Moved back to main function
        # strID, strTitle, strArtist = IO.add_inventory()
        intID = int(cd_id)
        dicRow = {'ID': intID, 'Title': cd_title, 'Artist': cd_artist}
        table.append(dicRow)

    @staticmethod
    def del_entry(cd_id, table):
        """Function to manage the deletion of entries to the existing table
        
        Deletes entries of the existing table after the user uses the 'd' functionality
        built into the script.
        
        Args:
            cd_id: the integer ID of the CD
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
            
        Returns:
            None
       
        """
        # intIDDel = IO.del_inventory()
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == cd_id:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed!\n')
        else:
            print('Could not find this CD!\n')
        
class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def load_file(file_name, table):
        """Function to manage initial data ingestion from file to a list of dictionaries
        
        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
            
        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
            
        """
        with open(strFileName, 'rb') as fileObj:
            table = pickle.load(fileObj)
        return table
        
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        """
        strYes = IO.load_inventory()
        if strYes == 'yes':
            with open(strFileName, 'rb') as fileObj:
                 table = pickle.load(fileObj)   
            return table
        else:
            input('The file was NOT loaded. Press [ENTER] to return to the menu.')
            return table

    @staticmethod
    # We should pass in the data the function needs
    # def write_file():
    def write_file(file_name, table):
        """Function to manage data output to file from a list of dictionaries
        
        Writes the table data to file identified as file_name from a 2D table.
        (list of dicts) table one line in the file represents one dictionary row in table.
        
        Args:
            file_name (string): name of file used to write data to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns:
            None.
        
        """
        strYesNo = IO.save_inventory()
        if strYesNo == 'y':
            # 3.6.2.1 save data
            with open(file_name, 'wb') as fileObj:
#            for row in table:
                pickle.dump(lstTbl, fileObj)
#                list(row.values())
#                lstValues[0] = str(lstValues[0])
#                objFile.write(','.join(lstValues) + '\n')
#            objFile.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
       
        """
        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to File\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection.
        Forces selection of one of the displayed letter options.

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x
        
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table.

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print()
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)')
        for row in lstTbl:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        print()

    
    @staticmethod
    # def add_inventory():
    # Renaming since it's not adding to inventory so much as returning user input
    def get_input():
        """Collects a user input to add a CD to the current inventory table.
        Verifies that the ID is an integer and that the Title and Artist
        fields are not blank.
        
        Args:
            None.

        Returns:
            strID: the integer ID of the CD
            strTitle: the title of the CD
            strArtist: the CD artist's name
            
        """
        # Checks for an integer input
        strID = ''
        while True:
            strID = input('Enter ID: ').strip()
            try:
                strID = int(strID)
                strID/1
                break
            except ValueError:
                print('Input must be an integer!')
       # Checks for a non-empty input
        strTitle = ''
        while True:
            strTitle = input('What is the CD\'s title? ').strip()
            try:
                if not strTitle:
                    raise ValueError('Empty String')
                break
            except ValueError:
                print('A non-zero input is required!')
        # Checks for a non-empty input
        strArtist = ''
        while True:
            strArtist = input('What is the Artist\'s name? ').strip()
            try:
                if not strArtist:
                    raise ValueError('Empty String')
                break
            except ValueError:
                print('A non-zero input is required!')
        return strID, strTitle, strArtist
    
    @staticmethod
    def del_inventory():
        """Collects a user input to delete a CD from the current inventory table.
        Verifies that the ID is an integer.
        
        Args:
            None.
            
        Returns:
            intIDDel: the integer ID of the CD to be deleted.
            
        """
        # Checks for an integer input
        intIDDel = ''
        while True:
            intIDDel = input('Which ID would you like to delete? ').strip()
            try:
                intIDDel = int(intIDDel)
                intIDDel/1
                break
            except ValueError:
                print('Input must be an integer!')
        print()
        return intIDDel
    
    @staticmethod
    def save_inventory():
        """Writes the contents of the current inventory to file.
        
        Args:
            None.
            
        Returns:
            strYesNo: the user selection for saving.
        
        """
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        print()
        return strYesNo
    
    @staticmethod
    def load_inventory():
        """Processes the user input when loading a file.
        
        Args:
            None.
        
        Returns:
            table: the data loaded from strFileName
        
        """
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        # Checks for a 'yes' input
        
        strYes= input('Type \'yes\' to continue and reload from file. Otherwise loading will be canceled: ').strip().lower()
        print()
        return strYes
       
# 1. When program starts, read in the currently saved Inventory
import pickle
lstTbl = FileProcessor.load_file(strFileName, lstTbl)
IO.show_inventory(lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
#        IO.load_inventory()
        lstTbl = FileProcessor.read_file(strFileName, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # 3.3.2 Add item to the table   
        # We should keep these function separate and pass the data between them.
        strID, strTitle, strArtist = IO.get_input()
        DataProcessor.add_entry(strID, strTitle, strArtist, lstTbl)
        # Display the inventory post-entry addition.
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        # 3.5.2 search thru table and delete CD
        # Same thing, keep the data entry in the IO section and separate from the processing.
        id_to_remove = IO.del_inventory()      
        DataProcessor.del_entry(id_to_remove, lstTbl)
        # Show inventory post-deletion
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        # 3.6.2 Process choice
        # 3.6.2.1 save data
        FileProcessor.write_file(strFileName, lstTbl)
        # FileProcessor.write_file()              
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




