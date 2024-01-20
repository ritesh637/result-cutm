from time import sleep
import pandas as pd
import os
import sqlite3
import subprocess
import sys
# from colorama import Fore, Back, Style


def welcome_message():

    print("""
__________                    .__   __     ____ ___        .__                    .___ ___________           .__   
\______   \ ____   ________ __|  |_/  |_  |    |   \______ |  |   _________     __| _/ \__    ___/___   ____ |  |  
 |       _// __ \ /  ___/  |  \  |\   __\ |    |   /\____ \|  |  /  _ \__  \   / __ |    |    | /  _ \ /  _ \|  |  
 |    |   \  ___/ \___ \|  |  /  |_|  |   |    |  / |  |_> >  |_(  <_> ) __ \_/ /_/ |    |    |(  <_> |  <_> )  |__
 |____|_  /\___  >____  >____/|____/__|   |______/  |   __/|____/\____(____  /\____ |    |____| \____/ \____/|____/
        \/     \/     \/                            |__|                   \/      \/                              """)
    print("\n Version 1.0 By - Ashish Github: ashish-devv \n")


def exitmessage():
    print("""
    __________                __________               
\______   \___.__. ____   \______   \___.__. ____  
 |    |  _<   |  |/ __ \   |    |  _<   |  |/ __ \ 
 |    |   \\___  \  ___/   |    |   \\___  \  ___/ 
 |______  // ____|\___  >  |______  // ____|\___  >
        \/ \/         \/          \/ \/         \/  """)

    print("\n Version 1.0 By - Ashish Github: ashish-devv \n")


def listallresultfiles():
    dir_list = os.listdir("./results")
    # print all excel file names with number
    filelist = []
    for i in range(len(dir_list)):
        if(dir_list[i].endswith(".xlsx")):
            filelist.append(dir_list[i])
            print(str(i) + ": " + dir_list[i])
    return filelist

# empty a sqlite database or create a new one


def createorempty():
    conn = sqlite3.connect('a.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS sheet1")
    c.execute("CREATE TABLE sheet1 ('SlNo.' INTEGER , 'REGD.NO' REAL, 'NAMEOFTHESTUDENT' TEXT, 'Sem' TEXT, 'SUB.CODE' TEXT, 'SUBJECTNAME' TEXT, 'Type' TEXT, 'Credit' TEXT ,'Grade' TEXT )")
    conn.commit()
    conn.close()


def printinstruction():
    print("""
    1. Empty the Existing Database or Create a New One
    2. List all the Result Files (Excel Files in Results Folder)
    3. Read All files in the Folder and Convert them to SQLite Database
    4 . Insert a Single File to SQLite Database
    5. Exit
    6. Save Changes in Git
    Press 'ctrl + c' to exit....
    """)


# read all excel files in the folder ,skip first row in each file and insert them to existing sqlite database with table name sheet1 and column names as mentioned in the table
def readallfiles(filelist):
    for i in range(len(filelist)):
        print("Inserting :: " + filelist[i] + " to SQLite Database")
        df = pd.read_excel("./results/" + filelist[i], names=[
                           "SlNo.", "REGD.NO", "NAMEOFTHESTUDENT", "Sem", "SUB.CODE", "SUBJECTNAME", "Type", "Credit", "Grade"])
        df.to_sql('sheet1', con=sqlite3.connect(
            'a.db'), if_exists='append', index=False)
    print("\nAll files are inserted to SQLite Database")


def insert_to_sqlite(filename):
    print("Inserting :: " + filename + " to SQLite Database")
    df = pd.read_excel("./results/" + filename, names=[
                       "SlNo.", "REGD.NO", "NAMEOFTHESTUDENT", "Sem", "SUB.CODE", "SUBJECTNAME", "Type", "Credit", "Grade"])
    df.to_sql('sheet1', con=sqlite3.connect(
        'a.db'), if_exists='append', index=False)


def saveChangesInGit():
    print("Saving Changes in Git")
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "\"Automatic Commit\""])
    subprocess.call(["git", "push"])
    print("Changes are saved in Git... and pushed to remote repository")


if __name__ == '__main__':
    try:
        if(len(sys.argv) > 1):
            if(sys.argv[1] == "run"):
                print("\n Starting the Application \n")
                welcome_message()
                createorempty()
                filelist = listallresultfiles()
                readallfiles(filelist)
        else:
            print(
                "\n Starting the Application \n")
            # sleep
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            while(True):
                welcome_message()
                printinstruction()
                choice = int(input("Enter your choice: "))
                # check if the choice is valid
                if(choice == 1):
                    createorempty()
                    print("Database Created")
                elif(choice == 2):
                    filelist = listallresultfiles()
                elif(choice == 3):
                    createorempty()
                    filelist = listallresultfiles()
                    readallfiles(filelist)
                elif(choice == 4):
                    while(True):
                        print("List of all files in the folder: ")
                        filelist = listallresultfiles()
                        choiceoffile = int(
                            input("Enter the file number to insert: "))
                        insert_to_sqlite(filelist[choiceoffile-1])
                        print("\nFile inserted to SQLite Database")
                        choice = int(
                            input("\nDo you want to insert more files? (1: Yes, 2: No): "))
                        if(choice == 2):
                            break
                elif(choice == 5):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    exitmessage()
                    break
                elif(choice == 6):
                    saveChangesInGit()
                else:
                    print("Invalid Choice")
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        exitmessage()
