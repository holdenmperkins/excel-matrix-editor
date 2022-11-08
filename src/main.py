import pandas as pd
import time
import os
import shutil
import sys
BasePath = sys.argv[1]
filenames = []

for file in os.listdir(BasePath + "/input"):
    if file.lower().endswith(".csv"):
        filenames.append(file)

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

fileIndex = 0
for file in filenames:
    print('Loading file: ' + file + '... ')
    fileIndex = fileIndex + 1
    timestr = time.strftime("%Y%m%d-%H%M%S")
    excelInputFile = BasePath + '/input/' + file
    input_df = pd.read_csv(excelInputFile)

    numberOfExRows = input_df.groupby('ex').size().values[0]
    numberOfUniqueEx = len(pd.unique(input_df['ex']))
    input_array = input_df.to_numpy()

    numberOfInputRows = len(input_df.index)
    if numberOfInputRows != (numberOfUniqueEx * numberOfExRows):
        print('Your file contains an error. numberOfInputRows != (numberOfUniqueEx * numberOfExRows). Make sure your file has headers in the data. Please see the example file.')
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
    df.to_excel(excel_writer = BasePath + "/output/" + timestr + '-' + str(fileIndex) +".xlsx", index=False, header=False)
    print(file + ' complete!')
    shutil.copy(excelInputFile, BasePath + '/archive')
    os.remove(excelInputFile)
    print(file + ' moved to archive')

print('Processing has finished. Please check the output directory for the finished file.')