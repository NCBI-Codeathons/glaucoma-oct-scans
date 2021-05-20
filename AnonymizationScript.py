import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import csv

"""print(os.listdir('/Users/binhvu/Downloads/CODEATHONIII/CODEATHONGLAUCOMA/Abudu91553621'))"""

"""
    WHAT THIS DOES: IT TAKES AN UNEDITTED DIRECTORY CALLED CODEATHON III AND DEREFERENCES THE PATIENTS WITHIN THE 
    FOLDERS 'CODEATHON GLAUCOMA' AND 'CODEATHON NORMAL'. IT CHANGES THE NAME OF THE FOLDERS FROM 'PATIENT LAST NAME +
    NUMBERS' TO 'P + PATIENT IDENTIFIER NUMBER'. IT CHANGES THE NAME OF THE SCANS INSIDE THE PATIENT FOLDER TO THEIR 
    PATIENT IDENTIFIER + WHAT SCAN IT IS' EX. P1 DISC OD.PNG. 
    IT ALSO SAVES INTO A CSV FILE (PATIENT IDENTIFIER: PATIENT NAME) 
    AND SAVES INTO ANOTHER CSV FILE (PATIENT IDENTIFIER: SEX, GLAUCOMA STATUS)

    HOW TO USE:
    1. DOWNLOAD AND UNZIP THE UN-EDITTED DIRECTORY CONTAINING ONLY CODEATHON GLAUCOMA AND CODEATHON NORMAL DATA
        - (NOTE: IF THE NAME OF THE DIRECTORY IS NOT NAMED 'CODEATHON III' AND THE FOLDERS INSIDE ARE NOT CALLED 
        CODEATHON GLAUCOMA AND CODEATHON NORMAL, THE VARIABLES 'PATH' AND 'PATH2' MUST BE CHANGED TO THE CORRECT PATH 
        WHERE THE FILES STAY. 'PATH 2' IS FOR THE NORMAL FOLDER AND 'PATH' IS FOR THE GLAUCOMA FOLDER.
    2. GO TO THE MAIN METHOD AND CHANGE THE FILE NAME PARAMETERS FOR THE 'SETTINGUPDATAFIRSTTIME' METHOD TO WHERE YOU
        WOULD LIKE TO SAVE THE DATA. THE FIRST PARAMETER SHOULD BE CHANGED TO WHERE YOU WOULD LIKE THE GLAUCOMA DATA
        TO BE SAVED TO WHILE THE SECOND PARAMETER SHOULD BE CHANGED TO WHERE YOU WOULD LIKE THE PATIENT IDENTIFIER 
        DATA TO BE SAVED TO.
    3. """

Males = {}


def SettingUpDataFirstTime(GlaucomaFile, PatientIdentifierFile):
    i = 0  # PATIENT IDENTIFIER COUNTER

    changingScan = {"1.png": "_Superficial_OD_", "2.png": "_Deep_OD_", "3.png": "_CC_OD_", "4.png": "_Disc_OD_",
                    "5.png": "_Superficial_OS_", "6.png": "_Deep_OS_", "7.png": "_CC_OS_", "8.png": "_Disc_OS_",

                    }

    PatientIdentifier = {'P0': {'name': 'Jane Doe'}}

    GlaucomaData = {'P0': {'Glaucoma Status': 'True', 'sex': 'null'}}
    k = ''
    PATH = '/Users/binhvu/Downloads/CODEATHON III/CODEATHON GLAUCOMA'
    PATH2 = '/Users/binhvu/Downloads/CODEATHON III/CODEATHON NORMAL'
    badfile = False
    for filename in os.listdir(PATH):

        filepath = os.path.join(PATH, filename)
        pii = 'p' +str(i)
        PatientIdentifier[pii] = {'name': str(filename)}
        GlaucomaData[pii] = {'Glaucoma Status': 'True', 'sex': 'null'}
        if filename.startswith('.'):
            print(filename)
            badfile = True
        else:

            for fn2 in os.listdir(filepath):
                source = os.path.join(filepath, fn2)
                split_file_name = fn2.split('Angio')

                new_name = 'p' + str(i) + " " + split_file_name[1]

                keyfinder = new_name[-5:]
                newnew_name = new_name.split('_20')

                if keyfinder in changingScan.keys():
                    k = changingScan[keyfinder]

                final_name = newnew_name[0] + k + '.png'
                os.rename(source, os.path.join(filepath, final_name))

        pi = 'p' + str(i)

        if badfile:
            i -= 1
            badfile = False
        i += 1

    for filename in os.listdir(PATH2):

        filepath = os.path.join(PATH2, filename)
        pii = 'p' +str(i)
        PatientIdentifier[pii] = {'name': filename}
        GlaucomaData[pii] = {'Glaucoma Status': 'False', 'sex': 'null'}

        if filename.startswith('.'):
            print(filename)
            badfile = True
        else:

            for fn2 in os.listdir(filepath):
                source = os.path.join(filepath, fn2)
                split_file_name = fn2.split('Angio')

                new_name = 'p' + str(i) + " " + split_file_name[1]

                keyfinder = new_name[-5:]
                newnew_name = new_name.split('_20')

                if keyfinder in changingScan.keys():
                    k = changingScan[keyfinder]

                final_name = newnew_name[0] + k + '.png'
                print(final_name)
                os.rename(source, os.path.join(filepath, final_name))

        if badfile:
            i -= 1
            badfile = False
        i += 1

    PatientIdentifier_save = pd.DataFrame(data=PatientIdentifier, ).T  # need to fix

    GlaucomaData_save = pd.DataFrame(data=GlaucomaData, ).T
    PatientIdentifier_save.to_csv(PatientIdentifierFile)
    GlaucomaData_save.to_csv(GlaucomaFile)


def main():
    SettingUpDataFirstTime('Glaucomafile.csv', 'PatientIdentifierFile.csv')


if __name__ == "__main__":
    main()
