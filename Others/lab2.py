import os

folders = input("Please provide the list of the folders by providing space in between them: ").split()

try:
    for i in folders:
        reslut = os.listdir(i)
        print("Listing the folder from " + i)
        #print(reslut)
        for finalresult in reslut:
            print(finalresult)
except FileNotFoundError:
    print("Please provide the valid folder name " + i)
except PermissionError:
    print("Not have the valid permission " + i)