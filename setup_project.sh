pip install -r src/requirements.txt
python -m venv python-matrix
source python-matrix/bin/activate
py2applet --make-setup src/matrix-converter.py --iconfile src/matrix.icns
python setup.py py2app -A
