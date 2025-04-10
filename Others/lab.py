# Listing the folders as per the use input

#Module Import

import os

#Defining the User Input statement

folders = input("Please provide the folders name by providin the space between them to list: ").split()
for i in (folders):
    result = os.listdir(i)
    print ("Listing the Folder in " + i)
    #print (result)
    for finalresult in (result):
        print(finalresult)
    
