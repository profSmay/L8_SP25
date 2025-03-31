#region imports
from Wing_Class import Wing
#endregion

#region function definitions
def main():
    # get the filename using the OPEN dialog
    filename = 'Wing Input File - good Loads.txt'
    #filename = 'Wing Input File - bad Loads.txt'
    f1 = open(filename, 'r')  # open the file for reading
    data = f1.readlines()  # read the entire file as a list of strings
    f1.close()  # close the file  ... very important
    wing=Wing()
    #The try-except structure is for error handling.
    try:  # some code that might fail
        wing.processWingData(data)
        print(wing.generate_report())
    except:  # what to do if the try block fails
        print('Bad File')

#endregion

main()