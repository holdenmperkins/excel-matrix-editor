# excel-matrix-editor
# Holden Perkins

First steps:

1) Make sure to install all dependencies.

2) Edit The two "/path/to/project/" portions of the file. These should be replaced with the path to the project directory on your machine.

  [NOTE] To run this program from the terminal rather than via the run.sh file simply copy the command contained in the run.sh file and paste it into terminal.

This project contains four directories.

  - input : This is where the initial file to be edited will be placed. Do not worry about the file name. The program will process all .csv files within this directory. 
  - output : The results of the program will be placed in this directory. The file names will be the current date and time with an appended index.
  - archive : After an input file is finished the file will be moved to this directory. 
   [WARNING] *If the file name already exists any previous files with the same name will be over written.*
  - src : This file contains the source code for the project.
  
  
  To run the program
  
    1) complete all "First steps"
    2) place your .csv file in the input directory
    3) double click on the run.sh file
    4) program will print "Processing has finished. Please check the output directory for the finished file." when it has finished
    5) check the output directory for results

python -m venv python-matrix  
source python-matrix/bin/activate
py2applet --make-setup matrix-converter.py
python setup.py py2app -A   