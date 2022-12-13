# excel-matrix-editor
# Holden Perkins

Initial setup:

1) Install all dependencies with the following command in the /src folder
    pip install -r requirements.txt 

2) Create a Python Virtual enviroment with the following command
    python -m venv python-matrix 

3) Activate the Python Virtual environment with the following command
    source python-matrix/bin/activate

4) Create the setup.py file with the following command (select Y if asked to replace the current setup.py file)
    py2applet --make-setup src/matrix-converter.py --iconfile src/matrix.icns

5) Generate the .app file (executable) with the following command
    python setup.py py2app -A

6) open the .app file to run the program. The file will be located here
    /src/dist/matrix-converter.app


This project contains four directories.

  - input : This is where the initial file to be edited will be placed. Do not worry about the file  name. The program will process all .csv files within this directory. 
  - output : The results of the program will be placed in this directory. The file names will be the current date and time with an appended index.
  - archive : After an input file is finished the file will be moved to this directory. 
   [WARNING] *If the file name already exists any previous files with the same name will be over written.*
  - src : This file contains the source code for the project.
  