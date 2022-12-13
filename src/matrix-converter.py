import sys
import tkinter as tk
from tkinter import filedialog, Label, PhotoImage
import pandas as pd
import time
import os
import shutil


window = tk.Tk()
BasePath = 'No/Path/Selected'
window.title('Matrix Converter')
AppIcon = PhotoImage(file = 'matrix.png')
window.iconphoto(False, AppIcon)

def getExValues(input_array, numberOfExRows):
    returnArray = []
    index = 0
    for row in input_array:
        if index == numberOfExRows - 1:
            returnArray.append(row[2])
            index = 0
        else:
            index = index + 1
    return returnArray

def getEmValues(input_array, numberOfExRows):
    returnArray = []
    index = 1
    for row in input_array:
        if index <= numberOfExRows:
            returnArray.append(row[1])
        index = index + 1
    return returnArray

def checkIfDirectoryExists(directory):
    MYDIR = (directory)
    CHECK_FOLDER = os.path.isdir(MYDIR)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
    else:
        print(MYDIR, "folder already exists.")

def getIntensityValues(input_array, numberOfExRows):
    returnArray = []
    index = 0
    currentIntensityArray = []
    for row in input_array:
        if index == numberOfExRows - 1:
            currentIntensityArray.append(row[3])
            returnArray.append(currentIntensityArray)
            currentIntensityArray = []
            index = 0
        else:
            currentIntensityArray.append(row[3])
            index = index + 1
    return returnArray

def setUserFeedback(feedback):
    print(feedback)
    global UserFeedback
    UserFeedback.config(text = feedback)


def runFileConvert(BasePath):
    checkIfDirectoryExists(BasePath + "/input")
    checkIfDirectoryExists(BasePath + "/output")
    checkIfDirectoryExists(BasePath + "/archive")
    filenames = []
    print(BasePath + "/input")
    for file in os.listdir(BasePath + "/input"):
        if file.lower().endswith(".csv"):
            filenames.append(file)
    fileIndex = 0
    print()
    for file in filenames:
        NewFileName = file.split('.csv')[0] + '-corrected'
        setUserFeedback('Loading file: ' + file + '... ')
        # print('Loading file: ' + file + '... ')
        fileIndex = fileIndex + 1
        timestr = time.strftime("%Y%m%d-%H%M%S")
        excelInputFile = BasePath + '/input/' + file
        input_df = pd.read_csv(excelInputFile)

        numberOfExRows = input_df.groupby('ex').size().values[0]
        numberOfUniqueEx = len(pd.unique(input_df['ex']))
        input_array = input_df.to_numpy()

        numberOfInputRows = len(input_df.index)
        if numberOfInputRows != (numberOfUniqueEx * numberOfExRows):
            # print('Your file contains an error. numberOfInputRows != (numberOfUniqueEx * numberOfExRows). Make sure your file has headers in the data. Please see the example file.')
            setUserFeedback('Your file contains an error. numberOfInputRows != (numberOfUniqueEx * numberOfExRows). Make sure your file has headers in the data. Please see the example file.')
            exit()

        ExValues = getExValues(input_array, numberOfExRows)
        EmValues = getEmValues(input_array, numberOfExRows)

        IntensityValues = getIntensityValues(input_array, numberOfExRows)

        row_index = 0
        ex_index = 0

        NumberOfEmValues = len(EmValues)
        HeaderArray = ['']
        for value in EmValues:
            HeaderArray.append(value)
        OutputMatrix = []
        OutputMatrix.append(HeaderArray)
        for x in range(numberOfUniqueEx):
            CurrentContentArray = [ExValues[x]]
            for value in IntensityValues[x]:
                CurrentContentArray.append(value)
            OutputMatrix.append(CurrentContentArray)

        df = pd.DataFrame(OutputMatrix).T
        df.to_excel(excel_writer = BasePath + "/output/" + NewFileName +".xlsx", index=False, header=False)
        # print(file + ' complete!')
        setUserFeedback(file + ' complete!')
        shutil.copy(excelInputFile, BasePath + '/archive')
        os.remove(excelInputFile)
        # print(file + ' moved to archive')
        setUserFeedback(file + ' moved to archive')

    # print('Processing has finished. Please check the output directory for the finished file.')
    setUserFeedback('Processing has finished. Please check the output directory for the finished file. \n' + BasePath + '/output')


def selectABasePath():
    BasePath_ = filedialog.askdirectory(initialdir = "/",title = "Select folder")
    PathLabel.config(text = BasePath_)
    global BasePath 
    BasePath = BasePath_
    print(BasePath_)

# runFileConvert(BasePath)

UserFeedback = Label(window, text = "")


SelectDirectoryBtn = tk.Button(window, text ="Select Base Directory", command=selectABasePath)
RunBtn = tk.Button(window, text ="Run Conversion", command=lambda:runFileConvert(BasePath))
Directions = Label(window, text = "First select a directory then, click run.")
PathLabel = Label(window, text = "no directory selected yet..")
Directions.pack()
PathLabel.pack()
SelectDirectoryBtn.pack()
RunBtn.pack()
UserFeedback.pack()
window.mainloop()